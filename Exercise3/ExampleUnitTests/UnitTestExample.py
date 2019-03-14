import torch
from SampleNetworks import ValueNetwork
from Worker import computeTargets, computePrediction
import csv
import math

def csvLoader(filename):
	result = []
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for row in reader:
			result.append(row)

	return result


if __name__ == "__main__":
	# For the sake of an example, set discount factor to 0.99
	discountFactor = 0.99

	# Load Data for Testing
	inputData = csvLoader("Input.csv")
	outputData = csvLoader("Output.csv")
	actionData = csvLoader("action.csv")
	rewardData = csvLoader("reward.csv")
	donesData = csvLoader("dones.csv")

	input_floats = [[float(c) for c in a] for a in inputData]
	output_floats_1 = [float(a[0]) for a in outputData ]
	output_floats_2 = [float(a[1]) for a in outputData ]

	action_ints = [int(c) for a in actionData for c in a ]
	reward_floats = [float(c) for a in rewardData for c in a ]
	dones_bool = [c == 'True' for a in donesData for c in a ]

	# Initialize example model for testing
	# During testing solution should be agnostic towards any model input/hidden layer size
	# However, provided model will always follow the DQN architecture, e.g. final layer has output equals to number of acts.

	example_model = ValueNetwork(20,[15,15],4)
	example_model.load_state_dict(torch.load('ExampleNetwork'))

	# Check for correctness	
	for a in range(len(input_floats)):
		pred_value = computePrediction(torch.Tensor([input_floats[a]]), action_ints[a], example_model).item()
		if not math.isclose(pred_value, output_floats_1[a], abs_tol=1e-3):
			print("Wrong Predicted Output")
			exit()
		print("Correct Predicted Output")

	for a in range(len(input_floats)):
		target_value = computeTargets(reward_floats[a], torch.Tensor([input_floats[a]]), discountFactor, dones_bool[a], example_model).item()
		if not math.isclose(target_value, output_floats_2[a], abs_tol=1e-3):
			print("Wrong Target Output")
			exit()
		print("Correct Target Output")
