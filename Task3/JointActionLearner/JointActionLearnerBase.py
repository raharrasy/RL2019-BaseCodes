#!/usr/bin/env python3
# encoding utf-8

import random
import argparse
from DiscreteMarlUtil.Environment import DiscreteMARLEnvironment
from DiscreteMarlUtil.Agent import Agent
from copy import deepcopy
import itertools
		
class JointQLearningAgent(Agent):
	def __init__(self, learningRate, discountFactor, epsilon, numTeammates, initVals=0.0):
		super(JointQLearningAgent, self).__init__()
		

	def setExperience(self, state, action, oppoActions, reward, status, nextState):
		
	def learn(self):

	def act(self):

	def setEpsilon(self, epsilon) :

	def setState(self, state):

	def toStateRepresentation(self, rawState):

if __name__ == '__main__':

	for itNum in range(args.numIterations):
		MARLEnv = DiscreteMARLEnvironment(numOpponents = args.numOpponents, numAgents = args.numAgents, seed=randomSeed)
		agents = []

		for i in range(args.numAgents):
			agent = JointQLearningAgent(learningRate = 0.1, discountFactor = 0.9, epsilon = 1.0, numTeammates=args.numAgents-1)
			agents.append(agent)

		numEpisodes = args.numEpisodes

		for episode in range(numEpisodes):	
			status = ["IN_GAME","IN_GAME","IN_GAME"]
			observation = MARLEnv.reset()
			
			for agent in agents:
				agent.setEpsilon(1.0 - min(1.0,episode/5000.0) * 0.95)
			
			while status[0]=="IN_GAME":
				actions = []
				stateCopies = []
				for agentIdx in range(args.numAgents):
					obsCopy = deepcopy(observation[agentIdx])
					stateCopies.append(obsCopy)
					agents[agentIdx].setState(agents[agentIdx].toStateRepresentation(obsCopy))
					actions.append(agents[agentIdx].act())

				nextObservation, reward, done, status = MARLEnv.step(actions)

				for agentIdx in range(args.numAgents):
					oppoActions = actions.copy()
					del oppoActions[agentIdx]
					agents[agentIdx].setExperience(agents[agentIdx].toStateRepresentation(stateCopies[agentIdx]), actions[agentIdx], oppoActions, 
						reward[agentIdx], status[agentIdx], nextObservation[agentIdx])
					agents[agentIdx].learn()
				
				observation = nextObservation