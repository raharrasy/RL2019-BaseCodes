#!/usr/bin/env python3
# encoding utf-8

from HFODefendingPlayer import HFODefendingPlayer
import random
import argparse
import ast


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--id', type=int, default=1)
	parser.add_argument('--numEpisodes', type=int, default=1000)
	args=parser.parse_args()

	hfoEnv = HFODefendingPlayer(agentId = args.id)
	hfoEnv.connectToServer()

	numEpisodes = args.numEpisodes

	# Get initial coordinates

	for episode in range(numEpisodes):
		hfoEnv.reset()
		status = 0
		while status==0:
			status = hfoEnv.doNOOP()

		if status == 5:
			hfoEnv.quitGame()
			break


