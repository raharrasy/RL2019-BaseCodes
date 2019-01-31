#!/usr/bin/env python3
# encoding utf-8

class MonteCarloAgent(Agent):
	def __init__(self, discountFactor, epsilon, initVals=0.0):
		super(MonteCarloAgent, self).__init__()

	def learn(self):
		raise NotImplementedError

	def toStateRepresentation(self, state):
		raise NotImplementedError

	def setExperience(self, state, action, reward, status, nextState):
		raise NotImplementedError

	def setState(self, state):
		raise NotImplementedError

	def reset(self):
		raise NotImplementedError

	def act(self):
		raise NotImplementedError

	def setEpsilon(self, epsilon):
		raise NotImplementedError


if __name__ == '__main__':

	raise NotImplementedError