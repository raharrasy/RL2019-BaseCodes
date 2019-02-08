import random
import copy
import pygame

class DiscreteMARLEnvironment(object):
	def __init__(self, numOpponents=0, numAgents=0, collisionPenalty = 0.4, visualize=False):
		self.opponentNums = numOpponents
		self.agentNums = numAgents
		self.collisionPenalty = collisionPenalty
		self.possibleActions = ['MOVE_UP', 'MOVE_DOWN', 'MOVE_LEFT', 'MOVE_RIGHT', 'KICK', 'NO_OP']
		self.curState = []
		self.agentInitLocs, self.opponentInitLocs = self.computeAgentInitLoc(), self.computeOpponentInitLoc()
		self.ballHolderId = None
		self.ballInitLocations = self.computeBallInitLoc()
		for idxAgents in range(numAgents):
			self.curState.append([copy.deepcopy(self.agentInitLocs), copy.deepcopy(self.opponentInitLocs), copy.deepcopy(self.ballInitLocations)])
		self.prevState = None
		self.dynamics = Dynamics()
		self.totalTimesteps = 500
		self.visualize = visualize
		if self.visualize:
			pygame.init()
			WINDOW_SIZE = (255, 255)
			self.screen = pygame.display.set_mode(WINDOW_SIZE)
			self.WIDTH = 20
			self.HEIGHT = 20
			self.MARGIN = 2
			pygame.display.set_caption("MARL Gridworld")
			self.clock = pygame.time.Clock()

	def reset(self):

		self.curState = []
		self.totalTimesteps = 500
		self.ballHolderId = None
		for idxAgents in range(self.agentNums):
			self.curState.append([copy.deepcopy(self.agentInitLocs), copy.deepcopy(self.opponentInitLocs), copy.deepcopy(self.ballInitLocations)])

		return self.curState

	def computeAgentInitLoc(self):
		agentLocs = []

		while len(agentLocs) < self.agentNums:

			randomXLoc = random.randint(0,1)
			randomYLoc = random.randint(0,4)

			if not [randomXLoc, randomYLoc] in agentLocs:
				agentLocs.append([randomXLoc,randomYLoc])

		return agentLocs

	def computeOpponentInitLoc(self):
		opponentLocs = []

		while len(opponentLocs) < self.opponentNums:

			randomXLoc = random.randint(3,4)
			randomYLoc = random.randint(0,4)

			if not [randomXLoc, randomYLoc] in opponentLocs:
				opponentLocs.append([randomXLoc,randomYLoc])

		return opponentLocs

	def computeBallInitLoc(self):
		randomXLoc = 2
		randomYLoc = random.randint(0,4)
		return [[randomXLoc, randomYLoc]]

	def act(self, actionStrings):

		self.prevState = copy.deepcopy(self.curState)
		nextLocations = []
		resultingStatus = "IN_GAME"
		counter = 0
		ballLocation = copy.deepcopy(self.curState[0][-1][0])

		for actionString in actionStrings:
			agentCurrentState = copy.deepcopy(self.curState[0][0][counter])
			actionString = self.dynamics.sampleDynamics(actionString, agentCurrentState)
			
			#ballOnPlayer = False
			if ballLocation == agentCurrentState and self.ballHolderId == None:
				self.ballHolderId = counter

			nextDiscX = agentCurrentState[0]
			nextDiscY = agentCurrentState[1]

			if actionString =='MOVE_UP':
				nextDiscY = max(agentCurrentState[1]-1,0)

			elif actionString =='MOVE_DOWN':
				nextDiscY = min(agentCurrentState[1]+1,4)


			elif actionString =='MOVE_LEFT':
				nextDiscX = max(0,agentCurrentState[0]-1)

			elif actionString =='MOVE_RIGHT':
				nextDiscX = min(4,agentCurrentState[0]+1)	

			agentNextLoc = [nextDiscX, nextDiscY]
			nextLocations.append(agentNextLoc)

			if self.ballHolderId != None:
				if counter == self.ballHolderId:
					ballLocation = [nextDiscX, nextDiscY]
			
			if actionString == 'KICK' or actionString == 'KICK_WAYWARD':
				if counter == self.ballHolderId:
					kickSuccessFlag = False
					if actionString == 'KICK':
						kickSuccessFlag = True
						self.curState = ["GOAL"]*self.agentNums
						resultingStatus = ["GOAL"]*self.agentNums
						return resultingStatus, self.curState
					else:
						self.curState = ["OUT_OF_BOUNDS"]*self.agentNums
						resultingStatus = ["OUT_OF_BOUNDS"]*self.agentNums
						return resultingStatus, self.curState
			counter += 1

		resultingState = []
		resultingState.append(copy.deepcopy(nextLocations))
		resultingState.append(copy.deepcopy(self.curState[0][1]))
		resultingState.append([copy.deepcopy(ballLocation)])

		self.curState = []
		for idxAgents in range(self.agentNums):
			self.curState.append(copy.deepcopy(resultingState))

		self.status = []
		for idxAgents in range(self.agentNums):
			self.status.append(resultingStatus)
		#beware of copying self.curState repeatedly

		return [resultingStatus]*self.agentNums, self.curState

	def get_reward(self, status, prevState, nextState):
		totalReward = 0

		if nextState[0] == "GOAL":
			#print("Prev State :", prevState)
			opponentLocs = prevState[0][1]
			agentLocs = prevState[0][0]

			if all([a in agentLocs for a in opponentLocs]) :
				totalReward += 1

		if nextState[0] != "GOAL" and nextState[0] != "OUT_OF_BOUNDS":
			ballLoc = nextState[0][-1][0]
			opponentLocs = nextState[0][1]

			if ballLoc in opponentLocs:
				totalReward -= self.collisionPenalty

		return [totalReward]*self.agentNums

	def step(self, action_params):
		status, nextState = self.act(action_params)
		if self.totalTimesteps == 0:
			status, nextState = ["OUT_OF_TIME"]*self.agentNums, ["OUT_OF_TIME"]*self.agentNums
		done = (status[0]!="IN_GAME")
		reward = self.get_reward(status, self.prevState, nextState)
		self.totalTimesteps -= 1
		return nextState, reward, [done]*self.agentNums, status
	
	def visualizeState(self, reward):
		self.screen.fill((0,0,0))
		visualized = self.curState
		if self.curState[0] == "GOAL" or self.curState[0] == "OUT_OF_BOUNDS":
			visualized = self.prevState
		for row in range(5):
			for column in range(5):
				color = (0, 255, 0)
				if [column, row] in visualized[0][1]:
					color = (255, 0, 0)
				if [column, row] in visualized[0][0]:
					color = (255, 255, 255)
				if [column, row] in visualized[0][2]:
					color = (0, 0, 255)
				if [column, row] in visualized[0][0] and [column, row] in visualized[0][2]:
					color = (127, 127, 255)
				if [column, row] in visualized[0][0] and [column, row] in visualized[0][1]:
					color = (255, 127, 127)
				if reward == 1 and [column, row] in visualized[0][2]:
					color = (255, 0, 255)
				pygame.draw.rect(self.screen, color,[(self.MARGIN + self.WIDTH) * column + self.MARGIN, (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
								     self.WIDTH,self.HEIGHT])
		self.clock.tick(60)
		pygame.display.flip()

class Dynamics(object):
	def __init__(self):
		self.dribbleDynamics = {"MOVE_UP":{"MOVE_UP" : 0.85, "MOVE_DOWN":0.05, "MOVE_LEFT":0.05, "MOVE_RIGHT":0.05},
								"MOVE_DOWN":{"MOVE_UP" : 0.05, "MOVE_DOWN":0.85, "MOVE_LEFT":0.05, "MOVE_RIGHT":0.05},
								"MOVE_LEFT":{"MOVE_UP" : 0.05, "MOVE_DOWN":0.05, "MOVE_LEFT":0.85, "MOVE_RIGHT":0.05},
								"MOVE_RIGHT":{"MOVE_UP" : 0.05, "MOVE_DOWN":0.05, "MOVE_LEFT":0.05, "MOVE_RIGHT":0.85},
								"NO_OP" :{"NO_OP" : 1.0}}


		self.kickDynamics = [[0.05,0.08,0.1,0.08,0.05],[0.15, 0.3,0.4,0.3,0.15],[0.25,0.5,0.6,0.5,0.25],[0.3,0.6,0.7,0.6,0.3],[0.2,0.8,0.9,0.8,0.2]]
	
	def setDribbleDynamics(self, dynamics):
		self.dribbleDynamics = dynamics

	def setKickDynamics(self, dynamics):
		self.kickDynamics = dynamics

	def sampleDynamics(self, action, location):
		if action == 'KICK':
			randomNum = random.random()
			goalProb = self.kickDynamics[location[0]][location[1]]
			if randomNum > goalProb:
				return 'KICK_WAYWARD'
			else:
				return 'KICK'

		else:
			nextActions = self.dribbleDynamics[action]
			nextAct = None
			sampledProb = random.random()

			for key in nextActions.keys():
				nextAct = key
				if sampledProb > nextActions[key]:
					sampledProb -= nextActions[key]
				else:
					break

			return nextAct
