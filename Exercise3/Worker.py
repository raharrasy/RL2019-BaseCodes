import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

from Networks import ValueNetwork
from torch.autograd import Variable
from Environment import HFOEnv
import random

def train():

def computeTargets(reward, nextObservation, discountFactor, done, targetNetwork):

def computePrediction(state, action, valueNetwork):
	
# Function to save parameters of a neural network in pytorch.
def saveModelNetwork(model, strDirectory):
	torch.save(model.state_dict(), strDirectory)
	




