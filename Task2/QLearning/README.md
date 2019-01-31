# Coursework 1 - SARSA Methods

You are required to implement the Q-Learning algorithm using the codes provided in `QLearningBase.py`. Before you proceed, install the HFO Domain first. Your task is to extend `QLearningBase.py` by implementing functions that have yet been implemented there.

## Specifications
### Automarking requirements
To ensure that your codes can be used by the marking script, ensure that all the necessary functions have been implemented. To check whether these implementations are correct, you can use the code snippet given in `__main__` to test your implementation. This code snippet gives an outline on how your implemented functions will interact to train a Q-Learning agent. If you just add some code to modify number of episodes and the hyperparameters for training, you can use this code to train a Q-Learning agent.

### Implemented Functions
#### `__init__`
This init function should initialize all the necessary parameters for training a Q-Learning Agent. This includes the learning rate, discount factor, and the epsilon value (if you use an epsilon greedy exploration strategy). This function will only be called once at the very beginning when you initialize agents for training.

### `learn()`
This is the most important function you need to implement in this task. This function has no input parameters. On the other hand, this method should return a single scalar that specifies the change in updated state-action value after you've trained your agents using Q-Learning's update. It will be used by the automarker to compare the correctness of your implementation against the solution.

### `act()`
This function will be used to choose the actions that your agents will use when faced with a state. It should only return the action that should be taken by the agent at the current state.

### `toStateRepresentation(state)`
You might want to use a different representation compared to the ones provided by the environment. This will provide a problem to the automarker. Therefore, you should implement a function that maps the raw state representation into the the state representation that you are using in your implementation. This function will receive a state and outputs it's value under the representations that you are using in your implementations.

### `setState(state)`
This function will be used to provide the agents you're controlling with the current state information. It will receive the state representation from the environment as an input. On the other hand, this does not need to output anything.

### `setExperience(state, action, reward, status, nextState)`
Once an agent executes an action, it will receive the rewards, status, and next states resulting from that action. Use this method to set these data to prepare your agent to learn using the Q-Learning update.

### `reset()`
You might want to reset some states of an agent at the beginning of each episode. Use this function to do that. This function does not require any inputs. Additionally, it also does not provide any outputs.

### `setLearningRate(learningRate)` and `setEpsilon(epsilon)`
This function should be used to set the learning rate and the epsilon (if you are using epsilon greedy) that you use during training. 
