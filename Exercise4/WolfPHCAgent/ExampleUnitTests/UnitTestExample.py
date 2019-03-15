from WolfPHCBase import WolfPHCAgent
import csv
import ast
from copy import deepcopy
import math

def csvLoader(filename):
	result = []
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for row in reader:
			result.append(row)

	return result


if __name__ == '__main__':
	
	inputData = csvLoader('Input.csv')
	outputData = csvLoader('Output.csv')

	# For the sake of an example, assume learning rate of 0.1, winDelta of 0.01 and loseDelta of 0.1
	learningRate = 0.1
	winDelta = 0.01
	loseDelta = 0.1

	# For this example, we are only using 1 episode
	numEpisodes = 1

	agents = []
	for i in range(2):
		agent = WolfPHCAgent(learningRate = 0.1, discountFactor = 0.9, winDelta=winDelta, loseDelta=loseDelta)
		agents.append(agent)

	for epsNum in range(numEpisodes):
		status = ["IN_GAME","IN_GAME"]
		totalReward = 0.0
		timeSteps = 0
		observation = ast.literal_eval(inputData[1][1])

		while status[0]=="IN_GAME":
			for agent in agents:
				agent.setWinDelta(winDelta)
				agent.setLoseDelta(loseDelta)
				agent.setLearningRate(learningRate)
			
			actions = []
			stateCopies = []

			for agentIdx in range(2):
				obsCopy = deepcopy(observation)
				stateCopies.append(obsCopy)
				agents[agentIdx].setState(agents[agentIdx].toStateRepresentation(obsCopy))
				actions.append(inputData[timeSteps+1][agentIdx+2])

			#In the unit test, act and the response from the environment will be computed by the line below

			#action = agent.act()
			#nextObservation, reward, done, status = MARLEnv.step(action)

			# But since we're using a predefined set of experience, load them from our storage

			try :
				nextObservation = ast.literal_eval(inputData[timeSteps+1][5])
			except:
				nextObservation = inputData[timeSteps+1][5]

			reward, done, status = float(inputData[timeSteps+1][4]),(inputData[timeSteps+1][6] == "True"), [inputData[timeSteps+1][7]]*2

			for agentIdx in range(2):
				agents[agentIdx].setExperience(agents[agentIdx].toStateRepresentation(stateCopies[agentIdx]), actions[agentIdx], 
					reward, status, agent.toStateRepresentation(nextObservation))
				learnRes = agents[agentIdx].learn()
				
				if not math.isclose(learnRes, float(outputData[timeSteps+1][agentIdx+1]), abs_tol=1e-4):
					print("Wrong Learn Output")
					exit()
				print("Correct Learn Output")

				averageUpdateOut = agents[agentIdx].calculateAveragePolicyUpdate()
				correctAvg = ast.literal_eval(outputData[timeSteps+1][agentIdx+3])
				correctAvg = [float(x) for x in correctAvg]

				for idx in range(len(averageUpdateOut)):
					if not math.isclose(averageUpdateOut[idx], correctAvg[idx], abs_tol=1e-4):
						print("Wrong Average Output")
						exit()
				print("Correct Average Output")

				correctPol = ast.literal_eval(outputData[timeSteps+1][agentIdx+5])
				correctPol = [float(x) for x in correctPol]

				policyOut = agents[agentIdx].calculatePolicyUpdate()
				for idx in range(len(policyOut)):
					if not math.isclose(policyOut[idx], correctPol[idx], abs_tol=1e-4):
						print("Wrong Policy Output")
						exit()
				print("Correct Policy Output")

				agentIdx += 1

			observation = nextObservation
			timeSteps += 1
	
