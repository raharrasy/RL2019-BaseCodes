class Agent(object):
	def __init__(self):
		self.possibleActions = ['MOVE_UP','MOVE_DOWN','MOVE_LEFT','MOVE_RIGHT','KICK','NO_OP']

	def act(self):
		""" Called at each loop iteration to choose and execute an action.
		Returns:
			None
		"""
		raise NotImplementedError

	def learn(self):
		""" Called at each loop iteration when the agent is learning. It should
		implement the learning procedure.
		Returns:
			None
		"""
		raise NotImplementedError
