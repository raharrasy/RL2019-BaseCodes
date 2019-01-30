class MDP(object):
	def __init__(self):

		# Possible states are e;ements of [0,1,...,5] x [0,1,...,5]
		# and two additional states to indicate GOALS and OUT (Wayward kicks)
		self.S = [(x,y) for x in range(5) for y in range(5)]
		self.S.append("GOAL")
		self.S.append("OUT")

		# Agent possible actions
		self.A = ["DRIBBLE_UP","DRIBBLE_DOWN","DRIBBLE_LEFT","DRIBBLE_RIGHT","SHOOT"]

		# Opposition locations
		self.oppositions = [(2,2), (4,2)]

		# Probability of scoring from locations in the pitch
		# each list inside goalProbs represents probability of scoring goal
		# for grids in a column, starting from the leftmost column
		self.goalProbs = [[0.00,0.00,0.0,0.00,0.00],[0.0, 0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0],[0.0,0.3,0.5,0.3,0.0],[0.0,0.8,0.9,0.8,0.0]]

	def getRewards(self, initState, Action, nextState):
		""" Return R(s,a,s') for the MDP 

		Keyword Arguments:
		initState -- The current state s.
		action -- The chosen action in state s, a.
		nextState -- The next state s'
		"""
		if nextState == "GOAL": # Rewards if agents managed to score a goal
			if initState != "GOAL":
				return 1
			else:
				return 0

		elif nextState == "OUT":
			if initState != "OUT":
				return -1
			else:
				return 0
		elif nextState in self.oppositions : # Rewards if agent bumped into opposition placed in (2,2) and (4,2)
			return -0.5
		else :
			return 0

	def probNextStates(self, initState, action):
		""" Return the next state probability for the MDP as a dictionary.

		Keyword Arguments:
		initState -- The current state s.
		action -- The chosen action in state s, a.

		"""
		nextStateProbs = {}
		if initState != "GOAL" and initState!="OUT":
			if action != "SHOOT":

				possibleDestinations = [(initState[0], max(0,initState[1]-1)),(initState[0], min(4,initState[1]+1)),
										(max(0,initState[0]-1), initState[1]), (min(4,initState[0]+1), initState[1])]

				intendedDestination = None
				if action == "DRIBBLE_UP":
					intendedDestination = (initState[0], max(0,initState[1]-1))
				elif action == "DRIBBLE_DOWN" :
					intendedDestination = (initState[0], min(4,initState[1]+1))
				elif action == "DRIBBLE_LEFT" :
					intendedDestination = (max(0,initState[0]-1), initState[1])
				else:
					intendedDestination = (min(4,initState[0]+1), initState[1])
			
				nextStateProbs[intendedDestination] = 0.8
				for intendedDestination in possibleDestinations :
					if not intendedDestination in nextStateProbs.keys():
						nextStateProbs[intendedDestination] = 0.0
					nextStateProbs[intendedDestination] += 0.05

			else :

				nextStateProbs["GOAL"] = self.goalProbs[initState[0]][initState[1]]
				nextStateProbs["OUT"] = 1.0-nextStateProbs["GOAL"]

		elif initState=="GOAL":
			nextStateProbs["GOAL"] = 1.0
		else:
			nextStateProbs["OUT"] = 1.0

		return nextStateProbs











