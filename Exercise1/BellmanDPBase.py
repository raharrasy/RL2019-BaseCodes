from MDP import MDP

class BellmanDPSolver(object):
	def __init__(self, discountRate):
		self.MDP = MDP()

	def initVs(self):

	def BellmanUpdate(self):

		raise NotImplementedError
		
if __name__ == '__main__':
	solution = BellmanDPSolver()
	for i in range(20000):
		values, policy = solution.BellmanUpdate()
	print("Values : ", values)
	print("Policy : ", policy)

