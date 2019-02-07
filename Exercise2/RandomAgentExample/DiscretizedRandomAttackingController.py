#!/usr/bin/env python3
# encoding utf-8

from DiscreteHFO.HFOAttackingPlayer import HFOAttackingPlayer
import random
import argparse


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--id', type=int, default=0)
	parser.add_argument('--numOpponents', type=int, default=0)
	parser.add_argument('--numTeammates', type=int, default=0)
	parser.add_argument('--numEpisodes', type=int, default=500)

	args=parser.parse_args()

	hfoEnv = HFOAttackingPlayer(numOpponents = args.numOpponents, numTeammates = args.numTeammates, agentId = args.id)
	hfoEnv.connectToServer()
	
	numEpisodes = 500
	for episode in range(numEpisodes+1):	

		status = 0
		observation = hfoEnv.reset()

		while status==0:
			act = random.randint(0,4)
			nextObservation, reward, done, status = hfoEnv.step(hfoEnv.possibleActions[act])
			observation = nextObservation

		if status == 5:
			hfoEnv.quitGame()
			break





