#!/usr/bin/env python3
# encoding utf-8

import os
import random
import itertools
import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--numTrials', type=int, default=500)
	parser.add_argument('--numPlayingDefenseNPCs', type=int, default=4)
	parser.add_argument('--numAgents', type=int, default=1)

	args=parser.parse_args()

	numTrials = args.numTrials
	numDefenseNPCs = args.numPlayingDefenseNPCs
	numAgents = args.numAgents

	f = open("initCoordinates.txt", "w")
	locs = [[0,2],[2,2]]

	for epsNumber in range(numTrials):
		f.write(str(locs)+'\n')

	f.close()
