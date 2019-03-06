# Exercise 3 - Asynchronous 1-Step Q-Learning with Function Approximation in HFO

## General Description

In this task, you are required to implement an attacking agent in the HFO domain that learns using the one-step Asynchronous Q-Learning  algorithm ([**Mnih et al., 2016**](https://arxiv.org/pdf/1602.01783.pdf)). Unlike variants of the Deep Q-Network algorithm, asynchronous training does not require you to use an experience replay to store the experiences encountered throughout the agent's learning process. However, it requires you to run multiple threads ("workers"), each having its own separate instance of the environment. 

In general, these are the different steps that needs to be done to implement an asynchronous Q-Learning agent:

1. Create a global value network which will later be periodically copied to the separate threads. 
2. Create separate threads, each equipped with a copy of the environment. 
3. In each thread, run the Q-Learning algorithm based on the value functions and calculate the updates using the gathered experiences.
5. Periodically push the gradients from the threads to the global network and update the global network parameters.


For this task, we will require you to store the parameters of your agent every **1 million global timesteps and the final parameters you get**. We will test the performance of your trained agent based on these submitted parameters. The performance of the agent will be measured based on average time to goal in each episode. In the event where your agent unsuccessfully scores a goal in an episode, we define the time to goal at that episode as the maximum allowed number of timesteps for that episode, which is 500 timesteps.

## Getting Started

### Starting an environment

The interface between agent and environment will be similar to previous tasks. You can find the necessary codes inside `Environment.py`. Since asynchronous training requires running several environments at once (one for each thread), each of your learning threads needs to initialize a single environment at the beginning. 

To start a new instance of an environment, you **must** use the following commands :

```
port = <Specified port number>
seed = <Specified seed number>
hfoEnv = HFOEnv(numTeammates=0, numOpponents=1, port=port, seed=seed)
hfoEnv.connectToServer()

# This runs a random agent
episodeNumber = 0
while True:
   action = random.randint(0,3)
   act = hfoEnv.possibleActions[action]
   newObservation, reward, done, status, info = hfoEnv.step(act)
   print(newObservation, reward, done, status, info)
                
   if done:
      episodeNumber += 1
```

During training, ensure that the port numbers of the different environments that you've initialized are different. If you use the same port numbers, one of the environment will not get initialized and you will get an error. Additionally, you'd also like the seeds of different environments to be different. This allows you to have different state distributions across different environments which provides a more stable gradient update for the agents.

### The HFO environment
   
#### State Space
You are allowed to define your own state spaces. However, your state spaces will mostly be based on HFO's `LOW_LEVEL_FEATURE_SET` and the `HIGH_LEVEL_FEATURE_SET`. You are free to use either one of them. Refer to the HFO manual to see the features provided in each feature set.

#### Action Spaces
You are to use the discrete actions provided by the HFO domain. These actions include `SHOOT`, `DRIBBLE`, `MOVE`, and `GO_TO_BALL`. You can find the exact specification on what each action does on the HFO manual. 

#### Reward Functions
You are allowed to define your own reward functions for this task. Make sure that your reward function enables faster learning for agents to score goals.

### Implementing your solution
#### Implemented Files (**Contains functions to be implemented**)
1. `Networks.py` 
   - Define the architecture of the **torch** neural network that you're using inside `__init__.py`
   - Define the forward computation used in your neural network inside `forward(inputs)`
2. `Environment.py` 
   - Implement your reward calculations inside `get_reward(status, nextState)`
   - Implement your state preprocessing function inside `preprocessState(state)`
3. `Worker.py`
   - Implement all the necessary computations required to train a single process of an agent inside `train()`
   - Implement the target value computation for Q-Learning inside `computeTargets(reward, nextObservation, discountFactor, done, targetNetwork)`. As you might see, this function should be usable for any target network architecture that you're using. **This function will be used in marking the correction of your implementation**.
   - Implement a single call for the forward computation of your Q-Network inside `computePrediction(state, action, valueNetwork)`. Note that this should be agnostic to any Q-Network architecture that you're using.
4. `main.py` 
   - This script should contain the necessary processes to run your asynchronous agent. We've provided an code snippet on how to asynchronously call multiple instances of the training function `train()` in `Worker.py` in the `__main__` function. 

#### Additional Scripts (**Might be useful for training**)
1. `SharedAdam.py`
   - We provide an example implementation of how to share pytorch optimizer statistics across multiple workers inside this function. In the original A3C paper, this reportedly produced better performance compared to using separate optimizers between threads. You are free to use this file or even create another shared optimizer implementation of the optimizer you've chosen.
   - Alternatively, initializing a separate optimizer for each thread is also an option. However, this might not perform as well as the shared optimizer. In this case, you can easily do this by initializing your favorite optimizer inside each of your threads (check out the torch.optim packages).

#### Environment Files
1. `Environment.py`
   - File to establish connections with HFO, define rewards for agents and preprocess state representations gathered from the HFO domain. Rewards and state representations can be derived from HFO's `LOW_LEVEL_FEATURE_SET` or `HIGH_LEVEL_FEATURE_SET`. You are allowed to choose any of them to base your rewards and states from. Just ensure that you've put the correct choice in line 56 of `Environment.py`. 
   - Apart from the part on choosing your state representation (line 56) and the implemented functions, other parts of `Environment.py` **should not be modified**.

2. `Goalkeeper.py` (**Should not be modified**)
   - An NPC Goalkeeper implementation for the environment. This NPC just runs around the goalposts throughout the episodes.

### Training your agents
Train your agents for up to 32 million timesteps. In this case, divide this equally between the number of threads that you are using. As an example, if you use 8 threads, then each thread will be responsible for up to 4 million timesteps. In this case, this means that you need to run the agents for 8000 episodes since each episode spans up to 500 timesteps.

### Marking details
#### Performance marking
The performance of the agent is going to be based on average time to goal. Under this metric, several different experiments with different starting states are executed. At each episode, we then measure the number of timesteps that passed until the agent scores a goal. In episodes where agents fail to score goals, a default value of the maximum timesteps in an episode (e.g. 500 timesteps) will be used for in the averaging process, otherwise the time to goal is going to be used.

**We require you to store the parameters of your neural network every 1 million global timesteps and at the end of training. Then, include it in your submitted files along with your scripts** under the name `**params_<k-th storage time>**`. To this end, we have provided you with a function to save your model parameters in `saveModelNetwork(model, strDirectory)` under `Worker.py`. As an example, **after 1 million global steps, store your parameters as `params_1`, `params_2` after 2 million global steps, etc**. At the end of training, save your parameters as **`params_last`**.

To save your model parameters, we have provided the saveModelNetwork() function inside `Worker.py`. You only need to specify the neural network that you are about to store and the name of the file for storage.

#### Unit test marking

We require you to implement two functions that are important to the predicted and target value computation in 1-step Q-Learning.
We will later test the correctness of **`computeTargets(reward, nextObservation, discountFactor, done, targetNetwork)`** and **`computePrediction(state, action, valueNetwork)`** inside `Worker.py`. These functions have the following inputs :

1. `computeTargets(reward, nextObservation, discountFactor, done, targetNetwork)`
   - reward, which is a float type data representing the reward achieved by the agent.
   - nextObservation, which is a 2D pytorch Tensor of the next states' feature representation.
   - discountFactor, which is a float type data representing the discounting factor used by the agent.
   - done, which is a boolean which indicates the end of the episode
   - targetNetwork, which is a pytorch model that will be used to compute the target values for the agents.

2. `computePrediction(state, action, valueNetwork)`
   - state, which is a 2D pytorch Tensor of the current states' feature representation.
   - action, which is a integer between 0 and 3 that denotes the index of the actions that are taken.
     - 0 denotes `MOVE`,
     - 1 denotes `SHOOT`,
     - 2 denotes `DRIBBLE`
     - 3 denotes `GO_TO_BALL`
   - valueNetwork, which is a pytorch model that will be used to compute the values for the agents.

For the outputs of this function, refer to the following example:
```
# As an example, we provide you with the following data in the unit test

rawStateRepresentation = [1.0, 2.0, 3.0]
stateRepresentation = [1.0, 2.0, 4.0]
reward = 1.0
discountFactor = 0.99
done = False

# Let's say agent chose the MOVE action
action = 0

state = torch.Tensor([rawStateRepresentation])
nextState = torch.Tensor([stateRepresentation])

# Call computePrediction to get predicted value of current state

curStatePrediction = computePrediction(state, action, valueNetwork)

# This line below should return the predicted value of taking action move at the specified state
actionValue = curStatePrediction.item()

# Call computeTargets to get predicted 1 step value of current state
targetPrediction = computeTargets(reward, nextState, discountFactor, done, targetNetwork)

# This line below should return the target value of state action pair
targetValue = targetPrediction.item()
```

During marking, using the same inputs, we will test the computed action values and the target values based on your implemented functions and see whether they are similar to our solution. This function should be agnostic to whatever state representation or model is used. 

Unit testing will be done by running two short episodes of interaction in the HFO environment and checking at each timestep the correctness of the outputs of your function. **The architecture used for testing will be similar to that which is used inside the DQN Algorithm.**

#### Suggested timeline
We understand that this exercise may seem daunting due to the many components that need to be implemented. However, it can be much easier if you go through the exercise following certain steps. In general, these are the steps that we recommend you to go through:

1. Getting prepared:
   - The exercise will be much easier if you understand how the HFO environment works and its python API. To achieve this, read the HFO Environment manual thoroughly and just take a look inside the example codes provided in `HFO/example`. This will probably take 3-4 hours of your time.

   - Familiarize yourself with pytorch. You don't need to be an expert in neural networks to get into this assignment. But you at least need to be familiar with how to create neural networks in pytorch and how to optimize them based on certain objective functions. To get to this point, read the [tutorials](https://pytorch.org/tutorials) in pytorch's official website. This will probably take 4-5 hours of your time.

   - Understand the asynchronous deep learning training framework. There's an excellent example for asynchronously training supervised learning models using pytorch provided [here](https://github.com/pytorch/examples/tree/master/mnist_hogwild). Use the codes provided here as the foundation for Asynchronous Q-Learning. Reading through this will probably require 2-3 hours of your time.

2. Implementing a minimum working implementation:
   - Don't get too much into details on state representations, rewards, and hyperparameter tuning at this point.
   - I strongly recommend just using a positive reward for goals and the standard state information provided by HFO. 
   - If your implementations are correct, even a simple linear model will show an improvement in performance.
   - This will probably take 25-30 hours of your time.
   - Also, use smaller learning rates. For example, try something like 1e-7 to 1e-4.

3. Now, improve your results by running experiments with different parameters, rewards, and state representations.

4. Strategically devise experiment schemes to better manage your time.
