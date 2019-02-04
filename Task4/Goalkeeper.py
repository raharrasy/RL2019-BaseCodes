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

class HFOGoalkeepingPlayer(object):
	def __init__(self, config_dir = '../../../bin/teams/base/config/formations-dt', 
		port = 6000, server_addr = 'localhost', team_name = 'base_right',
		play_goalie = True):

		self.hfo = HFOEnvironment()
		self.config_dir = config_dir
		self.port = port
		self.server_addr = server_addr
		self.team_name = team_name
		self.play_goalie = play_goalie
		self.destinationX = -9.0/11.0
		self.destinationY = 0.2
		
	def connectToServer(self):
		self.hfo.connectToServer(HIGH_LEVEL_FEATURE_SET,self.config_dir,self.port,self.server_addr,self.team_name,self.play_goalie)

	def moveToCorners(self):
		state =  self.hfo.getState()

		if ((state[0]+(9.0/11.0))**2 + (state[1]-0.2)**2)**0.5 < 0.01:
			self.destinationY = -0.2
		if ((state[0]+(9.0/11.0))**2 + (state[1]+0.2)**2)**0.5 < 0.01:
			self.destinationY = 0.2

		self.hfo.act(MOVE_TO, self.destinationX, self.destinationY)
		return self.hfo.step()

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--port', type=int, default=6000)
	parser.add_argument('--numEpisodes', type=int, default=500)
	args=parser.parse_args()

	numEpisodes = args.numEpisodes

	hfo = HFOGoalkeepingPlayer(port=args.port)
	hfo.connectToServer()

	for episode in range(numEpisodes):	
		status = 0
		while status==0:
			status = hfo.moveToCorners()

		if status == 5:
			hfo.hfo.act(QUIT)
			break
	
