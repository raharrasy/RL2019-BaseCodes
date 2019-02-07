# Exercise 2- SARSA Methods

You are required to implement the SARSA algorithm using the codes provided in `SARSABase.py`. Before you proceed,install the HFO Domain first by following the necessary steps outlined in `Task2/README.md`. Your task is to extend `SARSABase.py` by implementing functions that have yet been implemented in `SARSABase.py`.

## Specifications
### Automarking requirements
To ensure that your codes can be used by the marking script, ensure that all the necessary functions have been implemented. To check whether these implementations are correct, you **must** use the code snippet given in `__main__` to test your implementation. This code snippet gives an outline on how your implemented functions will interact to train a SARSA agent. Additionally, the same snippet is used in the automarking tools. In general, If you just add some code to modify number of episodes and the hyperparameters for training, you can use this code to train a SARSA agent.

Additionally, although the state-action values can be initialized using any value, you are to initialize the values as zeros for every state-action pair for automarking. 

### Implemented Functions
#### `__init__(self, learningRate, discountFactor, epsilon)`
This init function should initialize all the necessary parameters for training a SARSA Agent. This includes the learning rate, discount factor, and the epsilon value (if you use an epsilon greedy exploration strategy). This function will only be called once at the very beginning when you initialize agents for training.

#### `learn()`
This is the most important function you need to implement in this task. This function has no input parameters. On the other hand, this method **must** return a single scalar that specifies the change **(value after update subtracted by value before update)** in updated state-action value after you've trained your agents using SARSA's update. This function will be used in the automarker to compare the correctness of your implementation against the solution. **This function has the same functionality as line 9 in the books' SARSA pseudocode**


#### `act()`
This function will be used to choose the actions that your agents will use when faced with a state. It should only return the action that should be taken by the agent at the current state. **This function has the same functionality as line 5 in the books' SARSA pseudocode**
#### `setState(state)`
This function will be used to provide the agents you're controlling with the current state information. It will receive the state representation from the environment as an input. On the other hand, this does not need to output anything.

#### `setExperience(state, action, reward, status, nextState)`
Once an agent executes an action, it will receive the rewards, status, and next states resulting from that action. Use this method to set these data to prepare your agent to learn using the SARSA update. **This function has the same functionality as line 10 in the books' SARSA pseudocode**

#### `toStateRepresentation(state)`
You might want to use a different representation compared to the ones provided by the environment. This will provide a problem to the automarker. Therefore, you should implement a function that maps the raw state representation into the the state representation that you are using in your implementation. This function will receive a state and outputs it's value under the representations that you are using in your implementations.

#### `reset()`
You might want to reset some states of an agent at the beginning of each episode. Use this function to do that. This function does not require any inputs. Additionally, it also does not provide any outputs.

#### `setLearningRate(learningRate)` and `setEpsilon(epsilon)`
This function should be used to set the learning rate and the epsilon (if you are using epsilon greedy) that you use during training. 

#### `computeHyperparameters(numTakenActions, episodeNumber)`

This function should return a tuple indicating the learning rate and epsilon used at a certain timestep. This allows you to schedule the values of your hyperparameters and change it midway of training.

### Training process
To see how your implemented function interact with each other to train the agent, check the `__main__` function inside `SARSABase.py`. Make sure that you can successfully train your agent using the **exact same** codes inside `__main__` to ensure that your implementations are correct. This snippet of code used in `__main__` is also going to be used in the marking process.

## Marking details
### Performance marking
Using similar codes as what you've seen in `__main__`, we are going to run your agent on a randomly sampled MDP and compare it's performance to our solution. Performance is measured by running experiments using the same number of episodes at each experiment. We then average the rewards of the agent and plot this quantity.

### Unit test marking
We compare the results of updates from `learn()`. This function should return the difference between the value of the updated state-action pair after and before the update. (Q(s_t,a_t)(t+1) - Q(s_t,a_t)(t)) 
