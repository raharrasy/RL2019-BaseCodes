from QLearningBase import QLearningAgent
import csv
import ast
import math

def csvLoader(filename):
	result = []
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for row in reader:
			result.append(row)

	return result


if __name__ == '__main__':
	agent = QLearningAgent(learningRate = 0.1, discountFactor = 0.99, epsilon = 1.0)
	
	inputData = csvLoader('DataInput.csv')
	outputData = csvLoader('DataOutput.csv')

	# For the sake of an example, assume learning rate of 0.1
	learningRate = 0.1

	# Epsilon is not used since this example uses stored experience
	# But for the sake of an example, assume epsilon of 1

	epsilon = 1.0

	# For this example, we are only using 1 episode
	numEpisodes = 1

	for timestep in range(numEpisodes):
		status = 0
		timestep = 0
		observation = ast.literal_eval(inputData[1][1])

		while status == 0:
			agent.setEpsilon(epsilon)
			agent.setLearningRate(learningRate)
			nextObservation = None
			obsCopy = observation.copy()
			agent.setState(agent.toStateRepresentation(obsCopy))

			#In the unit test, act and the response from the environment will be computed by the line below

			#action = agent.act()
			#nextObservation, reward, done, status = hfoEnv.step(action)

			# But since we're using a predefined set of experience, load them from our storage

			action = inputData[timestep+1][2]
			try :
				nextObservation = ast.literal_eval(inputData[timestep+1][4])
			except:
				nextObservation = inputData[timestep+1][4]

			reward, done, status = float(inputData[timestep+1][3]),(inputData[timestep+1][5] == "True"), int(inputData[timestep+1][6])

			# Set the experience and learn
			agent.setExperience(agent.toStateRepresentation(obsCopy), action, reward, status, agent.toStateRepresentation(nextObservation))
			update = agent.learn()
			if not math.isclose(update, float(outputData[timestep+1][1]), abs_tol=1e-5):
				print("Wrong Output")
				exit()

			print("Correct Output")

			observation = nextObservation

			timestep += 1
	