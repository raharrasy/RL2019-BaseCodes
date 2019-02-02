#!/usr/bin/env python3
# encoding utf-8

import random
import argparse
from DiscMARLUtils.Environment import DiscreteMARLEnvironment
from DiscMARLUtils.Agent import Agent
from copy import deepcopy
		
class IndependentQLearningAgent(Agent):
	def __init__(self, learningRate, discountFactor, epsilon, initVals=0.0):
		super(QLearningAgent, self).__init__()

	def setExperience(self, state, action, reward, status, nextState):
	
	def learn(self):

	def act(self):

	def toStateRepresentation(self, state):

	def setState(self, state):

	def setEpsilon(self, epsilon):

if __name__ == '__main__':

	for itNum in range(args.numIterations):
		MARLEnv = DiscreteMARLEnvironment(numOpponents = args.numOpponents, numAgents = args.numAgents)
		agents = []
		for i in range(args.numAgents):
			agent = IndependentQLearningAgent(learningRate = 0.1, discountFactor = 0.9, epsilon = 1.0)
			agents.append(agent)

		numEpisodes = 50000

		for episode in range(numEpisodes):	
			status = ["IN_GAME","IN_GAME","IN_GAME"]
			observation = MARLEnv.reset()
			totalReward = 0.0
			timeSteps = 0
			for agent in agents:
				agent.setEpsilon(1.0 - min(1.0,episode/5000.0) * 0.95)
			
			while status[0]=="IN_GAME":
				actions = []
				stateCopies, nextStateCopies = []
				for agentIdx in range(args.numAgents):
					obsCopy = deepcopy(observation[agentIdx])
					stateCopies.append(obsCopy)
					agents[agentIdx].setState(agent.toStateRepresentation(obsCopy))
					actions.append(agents[agentIdx].act())

				nextObservation, reward, done, status = MARLEnv.step(actions)

				for agentIdx in range(args.numAgents):
					agents[agentIdx].setExperience(agent.toStateRepresentation(stateCopies[agentIdx]), actions[agentIdx], reward[agentIdx], 
						status[agentIdx], agent.toStateRepresentation(nextObservation[agentIdx]))
					agents[agentIdx].learn()
				
				observation = nextObservation
				