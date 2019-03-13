from MonteCarloBase import MonteCarloAgent
import csv
import ast
import math

def csvEpisodeLoader(filename):
	result = []
	epsData = []
	epsId = ""
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for row in reader:
			if row[0] != epsId:
				if epsData != []:
					result.append(epsData)
					epsData = []
				epsId = row[0]
			epsData.append(row)

		result.append(epsData)

	return result

def csvLoader(filename):
	result = []
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for row in reader:
			result.append(row)

	return result


if __name__ == '__main__':
	agent = MonteCarloAgent(discountFactor = 0.99, epsilon = 1.0)
	
	inputData = csvEpisodeLoader('Input.csv')
	outputData = csvLoader('Output.csv')

	numTakenActions = 0 

	# For the sake of an example, assume learning rate of 0.1
	learningRate = 0.1

	# Epsilon is not used since this example uses stored experience
	# But for the sake of an example, assume epsilon of 1

	epsilon = 1.0

	# For this example, we are only using 1 episode
	numEpisodes = 2

	for episode in range(numEpisodes):
		timestep = 0
		agent.reset()
		observation = ast.literal_eval(inputData[episode+1][timestep][2])
		status = 0
		
		while status == 0:
			agent.setEpsilon(epsilon)
			obsCopy = observation.copy()
			agent.setState(agent.toStateRepresentation(obsCopy))

			#In the unit test, act and the response from the environment will be computed by the line below

			#action = agent.act()
			#nextObservation, reward, done, status = hfoEnv.step(action)

			# But since we're using a predefined set of experience, load them from our storage

			action = inputData[episode+1][timestep][3]
			try :
				nextObservation = ast.literal_eval(inputData[episode+1][timestep][5])
			except:
				nextObservation = inputData[episode+1][timestep][5]

			reward, done, status = float(inputData[episode+1][timestep][4]),(inputData[episode+1][timestep][6] == "True"), int(inputData[episode+1][timestep][7])
			# Set the experience and learn
			agent.setExperience(agent.toStateRepresentation(obsCopy), action, reward, status, agent.toStateRepresentation(nextObservation))
			observation = nextObservation

			timestep += 1

		_ , update = agent.learn()
		result_list = ast.literal_eval(outputData[episode+1][1])

		for idx in range(len(result_list)):
			if not math.isclose(update[idx], float(result_list[idx]), abs_tol=1e-5):
				print("Wrong Output")
				exit()

		print("Correct Output")
	