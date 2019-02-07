#!/usr/bin/env python3
#encoding utf-8

from hfo import *
from copy import copy, deepcopy
from DiscreteHFO.EnvironmentDynamics import Dynamics
import math
import random
import ast

class HFOAttackingPlayer(object):
	def __init__(self, config_dir = '../../../bin/teams/base/config/formations-dt', agentId=0,
		port = 6000, server_addr = 'localhost', team_name = 'base_left', play_goalie = False,
		initDiscCoordX = 0, initDiscCoordY = 0, numOpponents = 0, numTeammates = 0, 
		collisionPenalty = 0.4, dribbleAccuracy = 0.2, kickAccuracy = [[0.8] * 5] * 5,
		actionDurations = 40, initFileLoc = "initCoordinates.txt"):

		self.hfo = HFOEnvironment()
		self.config_dir = config_dir
		self.port = port
		self.server_addr = server_addr
		self.team_name = team_name
		self.play_goalie = play_goalie
		self.initDiscCoordY = initDiscCoordY
		self.initDiscCoordX = initDiscCoordX
		self.numTeammates = numTeammates
		self.numOpponents = numOpponents
		self.collisionPenalty = collisionPenalty
		self.curState = None
		self.dribbleAccuracy = dribbleAccuracy
		self.kickAccuracy = kickAccuracy
		self.possibleActions = ['DRIBBLE_UP', 'DRIBBLE_DOWN', 'DRIBBLE_LEFT', 'DRIBBLE_RIGHT', 'KICK']
		self.actionDurations =  actionDurations
		self.initPositions = []
		self.oppoPositions = []
		self.agentId = agentId
		self.episode = 0
		self.initFileLoc = initFileLoc
		self.dynamics = Dynamics()
		self.readInitLocFinal()


	# Restarts episode by resetting the current state of the environment to the initial state.
	def reset(self):
		self.curState = [(self.initPositions[self.episode][0],self.initPositions[self.episode][1])]
		for oppoIndex in range(len(self.oppoPositions[self.episode])):
			self.curState.append((self.oppoPositions[self.episode][oppoIndex][0],self.oppoPositions[self.episode][oppoIndex][1]))
		
		self.initDiscCoordX = self.initPositions[self.episode][0]
		self.initDiscCoordY = self.initPositions[self.episode][1]
		self.initGame()
		self.episode += 1

		return self.curState		

	# Establish connection with HFO server
	def connectToServer(self):
		self.hfo.connectToServer(HIGH_LEVEL_FEATURE_SET,self.config_dir,self.port,self.server_addr,self.team_name,self.play_goalie)

	# From a location feature given by HFO, output the discrete representation of that location
	def getDiscretizedLocation(self, coordX, coordY):
                discCoordX = int(math.floor((coordX+(1.0/11.0))/0.34))
                discCoordY = int(math.floor((coordY)/0.275))

                return discCoordX, discCoordY

	# Based on gridworld coordinate, get the coordinates of the centroid of that
	# grid in the real HFO state representation.

	def getCentroidCoord(self, discCoordX, discCoordY):
                centroidX = (-1.0/1.1) + discCoordX * 0.34 + 0.17
                centroidY = -0.825 + discCoordY * 0.275 + 0.1375

                return centroidX, centroidY

	# Method to move agent to it's initial position

	def moveToInitLocs(self):
		destinationX, destinationY = self.getCentroidCoord(self.initDiscCoordX, self.initDiscCoordY)
		self.hfo.act(DRIBBLE_TO, destinationX, destinationY)
		self.hfo.step()
		#completeState = self.hfo.getState()
		#self.curState = self.process_state(completeState)

	# Method updates the discrete state representation of the environment after
	# the agent does an action. Stochaticity of the environment is implemented here.

	def act(self, actionString):

		resultingStatus = 0
		counter = 0
		agentCurrentState = self.curState[0]
		actionString = self.dynamics.sampleDynamics(actionString, agentCurrentState)
		if actionString =='DRIBBLE_UP':
			nextDiscX = self.curState[0][0]
			nextDiscY = max(self.curState[0][1]-1,0)


		elif actionString =='DRIBBLE_DOWN':
			nextDiscX = self.curState[0][0]
			nextDiscY = min(self.curState[0][1]+1,5)


		elif actionString =='DRIBBLE_LEFT':
			nextDiscX = max(0,self.curState[0][0]-1)
			nextDiscY = self.curState[0][1]

		elif actionString =='DRIBBLE_RIGHT':
			nextDiscX = min(4,self.curState[0][0]+1)
			nextDiscY = self.curState[0][1]
			

		if actionString != 'KICK' and actionString != 'KICK_WAYWARD':
			destinationX, destinationY = self.getCentroidCoord(nextDiscX, nextDiscY)

			for index in range(1, len(self.curState)):
				if (nextDiscX, nextDiscY) == self.curState[index]:
					destinationX -= 0.05
					destinationY -= 0.05
					break
			resultingStatus = self.visualizeDribbles(destinationX,destinationY)		
			self.curState[0] = (nextDiscX, nextDiscY)

		else :
			kickSuccessFlag = False
			if actionString == 'KICK':
				kickSuccessFlag = True
				self.curState = "GOAL"
				resultingStatus = GOAL
			else:
				self.curState = "OUT_OF_BOUNDS"
				resultingStatus = OUT_OF_BOUNDS

			self.visualizeKicks(kickSuccessFlag)



		return resultingStatus, self.curState

	# Visualizes the DRIBBLE_* actions taken by agent. Action is 
	# completed only if the environment decides to stop the game
	# or if the action duration surpasses self.actionDurations iterations.
	# Returns the status after the dribble action is completed

	def visualizeDribbles(self, destinationX, destinationY):
		resultingStatus =0
		counter = 0

		# Action will run as long as the number of iterations where it's done is less than
		# self.actionDurations and the ball doesn't get out of the game board.

		while counter < self.actionDurations and resultingStatus == 0:
			currentState = self.hfo.getState()
			# if agent does not have the ball agent must get closer to the ball
			# else, dribble to destinatination

			if currentState[5] != 1:
				self.hfo.act(GO_TO_BALL)
			else :
				self.hfo.act(DRIBBLE_TO, destinationX, destinationY)
			resultingStatus = self.hfo.step()
			counter += 1
		return resultingStatus

	# Visualizes the KICK action taken by agent. Action is 
	# completed only if the ball gets out of the play, the episode finishes,
	# or a goal happened.

	def visualizeKicks(self, kickSuccessFlag):
		resultingStatus = 0
		# If kick is successfully directed to goal
		if kickSuccessFlag:
			currentState = self.hfo.getState()
			status = 0
			while status == 0:

				# Shoot the ball to the goal
				self.hfo.act(SHOOT)
				status = self.hfo.step()
				currentState = self.hfo.getState()

				# In case that the kick is too weak, agent must chase the ball
				while currentState[5] != 1 and status == 0:
					self.hfo.act(GO_TO_BALL)
					status = self.hfo.step()
					currentState = self.hfo.getState()

		# If kick is wayward
		else:
			currentState = self.hfo.getState()
			status = 0
			while status == 0:

				# Shoot the ball to a point close to the agent which isn't
				# the goal
				curPosX, curPosY = currentState[0], currentState[1]
				if curPosX > 0 and curPosY > 0 :
					self.hfo.act(KICK_TO, 0.5, 1.0,3)
				elif curPosX <= 0 and curPosY > 0 :
					self.hfo.act(KICK_TO, -0.5, 1.0,3)
				elif curPosX > 0 and curPosY <= 0:
					self.hfo.act(KICK_TO, 1.0, -0.5,3)
				else:
					self.hfo.act(KICK_TO, -1.0, -0.5,3)

				# In case that the kick is too weak, agent must chase the ball
				status = self.hfo.step()
				currentState = self.hfo.getState()
				while currentState[5] != 1 and status == 0:
					self.hfo.act(GO_TO_BALL)
					status = self.hfo.step()
					currentState = self.hfo.getState()

		return resultingStatus

	# Defined reward for this environment
	# Add a -0.4 penalty if attacking agent occupies the same grid
	# as an attacking opponent. Also, give +1 for goal.
	def get_reward(self, status, nextState):
		totalReward = 0
		if status == GOAL:
			totalReward += 1

		if nextState != "GOAL" and nextState != "OUT_OF_BOUNDS":
			for index in range(1, len(nextState)):
				if nextState[0] == nextState[index]:
					totalReward -= self.collisionPenalty
					break

		return totalReward
		

	# Discretize the state representation given by the HFO environment.
	# Discretization is done to the locations of the ball and agents
	def process_state(self, state):
		discretizedState = self.getDiscretizedLocation(state[0], state[1])
		offset = 10 + 6*self.numTeammates

		infoList = [discretizedState]
		for i in range(self.numOpponents):
			oppoLocX = offset + 3*i
			oppoLocY = offset + 3*i + 1
			infoList.append(self.getDiscretizedLocation(state[oppoLocX],state[oppoLocY]))
		return infoList

	# Method that serves as an interface between a script controlling the agent
	# and the environment. Method returns the nextState, reward, flag indicating
	# end of episode, and current status of the episode

	def step(self, action_params):
		status, nextState = self.act(action_params)
		done = (status!=IN_GAME)
		reward = self.get_reward(status, nextState)
		return self.curState, reward, done, status

		
	def waste_one_episode(self):
		status = IN_GAME
		while status == IN_GAME:
			self.hfo.act(DASH, 0, 0)
			status = self.hfo.step()

	def waste_one_step(self):
		self.hfo.act(DASH, 0, 0)
		self.hfo.step()

	def quitGame(self):
		self.hfo.act(QUIT)

	# For the first 150 iterations, reposition agents
	# to initial position
	def initGame(self):
		frameCounters = 0
		while frameCounters < 150:
			self.moveToInitLocs()
			frameCounters += 1

	def readInitLocFinal(self):
		filename = self.initFileLoc
		file = open(filename, "r")

		self.initPositions = []

		for line in file:
			episodeOpponents = []
			listPos = ast.literal_eval(line)
			for index in range(self.numOpponents+1):
				if index == self.agentId:
					self.initPositions.append(listPos[index])
				else:
					episodeOpponents.append(listPos[index])
			self.oppoPositions.append(episodeOpponents)








