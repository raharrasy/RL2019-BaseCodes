#!/usr/bin/env python3
# encoding utf-8

import random
from DiscreteHFO.HFOAttackingPlayer import HFOAttackingPlayer
from DiscreteHFO.Agent import Agent
import argparse

class QLearningBase(Agent):
	def __init__(self, learningRate, discountFactor, epsilon, initVals=0.0):
		super(QLearningBase, self).__init__()
		

	def learn(self):
		raise NotImplementedError

	def act(self):
		raise NotImplementedError

	def toStateRepresentation(self, state):
		raise NotImplementedError

	def setState(self, state):
		raise NotImplementedError

	def setExperience(self, state, action, reward, status, nextState):
		raise NotImplementedError

	def setLearningRate(self, learningRate):
		raise NotImplementedError

	def setEpsilon(self, epsilon):
		raise NotImplementedError

	def reset(self):
		raise NotImplementedError

if __name__ == '__main__':
	raise NotImplementedError

	
