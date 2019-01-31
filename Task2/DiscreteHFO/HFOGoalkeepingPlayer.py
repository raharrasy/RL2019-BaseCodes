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
		port = 6000, server_addr = 'localhost', team_name = 'base_right', play_goalie = True):

		self.hfo = HFOEnvironment()
		self.config_dir = config_dir
		self.port = port
		self.server_addr = server_addr
		self.team_name = team_name
		self.play_goalie = play_goalie
		
	def connectToServer(self):
		self.hfo.connectToServer(HIGH_LEVEL_FEATURE_SET,self.config_dir,self.port,self.server_addr,self.team_name,self.play_goalie)

	def moveToCorner(self):
		self.hfo.act(MOVE_TO, -0.85,-0.85)
		return self.hfo.step()
	
