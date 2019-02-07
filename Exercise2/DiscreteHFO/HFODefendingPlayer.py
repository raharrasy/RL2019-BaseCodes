#!/usr/bin/env python3
#encoding utf-8

from hfo import *
import argparse
import ast
import numpy as np
import sys, os
import math
import random
from copy import copy, deepcopy

class HFODefendingPlayer(object):
	def __init__(self, config_dir = '../../../bin/teams/base/config/formations-dt', 
		port = 6000, server_addr = 'localhost', team_name = 'base_right', 
		initDiscCoordX = 0, initDiscCoordY = 0, numOpponents = 0, numTeammates = 0,
		agentId=0, initFileLoc="initCoordinates.txt"):


		self.hfo = HFOEnvironment()
		self.config_dir = config_dir
		self.port = port
		self.server_addr = server_addr
		self.team_name = team_name
		self.initDiscCoordY = initDiscCoordY
		self.initDiscCoordX = initDiscCoordX
		self.numTeammates = numTeammates
		self.numOpponents = numOpponents

		self.defenderLocations = None
		self.actionCounter = 0

		self.initPositions = []
		self.agentId = agentId
		self.episode = 0
		self.initFileLoc = initFileLoc
		self.readInitLocFinal()

	def reset(self):
		self.initDiscCoordX = 2-(self.initPositions[self.episode][0]-2)
		self.initDiscCoordY = 3-(self.initPositions[self.episode][1]-2)
		self.initGame()
		self.episode += 1

	def connectToServer(self):
		self.hfo.connectToServer(HIGH_LEVEL_FEATURE_SET,self.config_dir,self.port,self.server_addr,self.team_name,False)

	def getDiscretizedLocation(self, coordX, coordY):
		discCoordX = int(math.floor((coordX+(1.0/11.0))/0.34))
		discCoordY = int(math.floor((coordY)/0.275))
		return discCoordX, discCoordY
	
	def getCentroidCoord(self, discCoordX, discCoordY):
		centroidX = (-0.9/1.1) + discCoordX * 0.34 + 0.17
		centroidY = -0.825 + discCoordY * 0.275 + 0.1375
		return centroidX, centroidY

	def process_state(self, state):
		discretizedState = self.getDiscretizedLocation(state[0], state[1])
		offset = 10 + 6*self.numTeammates

		infoList = [discretizedState]
		for i in range(self.numOpponents):
			oppoLocX = offset + 3*i
			oppoLocY = offset + 3*i + 1
			infoList.append(self.getDiscretizedLocation(oppoLocX, oppoLocY))

	def moveToInitLocs(self):
		destinationX, destinationY = self.getCentroidCoord(self.initDiscCoordX, self.initDiscCoordY)
		completeState = self.hfo.getState()
		if abs(destinationX-completeState[0]) > 0.01 or abs(destinationY-completeState[1]) > 0.01:
			self.hfo.act(MOVE_TO, destinationX, destinationY)
		else:
			self.hfo.act(NOOP)
		self.hfo.step()
		completeState = self.hfo.getState()
		state = [completeState[0], completeState[1]]
		self.curState = self.process_state(completeState)

	def doNOOP(self):
		self.hfo.act(NOOP)
		return self.hfo.step()
		
	def waste_one_episode(self):
		status = IN_GAME
		while status == IN_GAME:
			self.hfo.act(DASH, 0, 0)
			status = self.hfo.step()
		prRed('Finally consumed this episode!')

	def waste_one_step(self):
		self.hfo.act(DASH, 0, 0)
		self.hfo.step()

	def quitGame(self):
		self.hfo.act(QUIT)

	def readInitLocFinal(self):
		filename = self.initFileLoc
		file = open(filename, "r")

		self.initPositions = []
		for line in file:
			self.initPositions.append(ast.literal_eval(line)[self.agentId])

	def initGame(self):
		frameCounters = 0
		while frameCounters < 150:
			self.moveToInitLocs()
			frameCounters += 1








