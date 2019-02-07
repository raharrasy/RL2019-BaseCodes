import random

class Dynamics(object):
	def __init__(self):
		self.dribbleDynamics = {"DRIBBLE_UP":{"DRIBBLE_UP" : 0.85, "DRIBBLE_DOWN":0.05, "DRIBBLE_LEFT":0.05, "DRIBBLE_RIGHT":0.05},
								"DRIBBLE_DOWN":{"DRIBBLE_UP" : 0.05, "DRIBBLE_DOWN":0.85, "DRIBBLE_LEFT":0.05, "DRIBBLE_RIGHT":0.05},
								"DRIBBLE_LEFT":{"DRIBBLE_UP" : 0.05, "DRIBBLE_DOWN":0.05, "DRIBBLE_LEFT":0.85, "DRIBBLE_RIGHT":0.05},
								"DRIBBLE_RIGHT":{"DRIBBLE_UP" : 0.05, "DRIBBLE_DOWN":0.05, "DRIBBLE_LEFT":0.05, "DRIBBLE_RIGHT":0.85}}


		self.kickDynamics = [[0.05,0.08,0.1,0.1,0.08,0.05],[0.05, 0.1,0.2,0.2,0.1,0.05],[0.15,0.25,0.35,0.35,0.25,0.15],[0.2,0.35,0.6,0.6,0.35,0.2],[0.35,0.7,0.9,0.9,0.7,0.35]]
	
	def setDribbleDynamics(self, dynamics):
		self.dribbleDynamics = dynamics

	def setKickDynamics(self, dynamics):
		self.kickDynamics = dynamics

	def sampleDynamics(self, action, location):
		if action == 'KICK':
			randomNum = random.random()
			goalProb = self.kickDynamics[location[0]][location[1]]
			if randomNum > goalProb:
				return 'KICK_WAYWARD'
			else:
				return 'KICK'

		else:
			nextActions = self.dribbleDynamics[action]
			nextAct = None
			sampledProb = random.random()

			for key in nextActions.keys():
				nextAct = key
				if sampledProb > nextActions[key]:
					sampledProb -= nextActions[key]
				else:
					break

			return nextAct
