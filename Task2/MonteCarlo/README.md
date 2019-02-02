# Coursework 1 - Monte Carlo Methods

You are required to implement the Monte Carlo algorithm using the codes provided in `MonteCarloBase.py`. Before you proceed, install the HFO Domain first. Your task is to extend `MonteCarloBase.py` by implementing functions that have yet been implemented there.

## Specifications
### Automarking requirements
To ensure that your codes can be used by the marking script, ensure that all the necessary functions have been implemented. To check whether these implementations are correct, you can use the code snippet given in `__main__` to test your implementation. This code snippet gives an outline on how your implemented functions will interact to train a Monte Carlo agent. If you just add some code to modify number of episodes and the hyperparameters for training, you can use this code to train a Monte Carlo agent.

### Implemented Functions
#### `__init__`
This init function should initialize all the necessary parameters for training a Monte Carlo Agent. This includes the discount factor and the epsilon value. This function will only be called once at the very beginning when you initialize agents for training.

### `learn()`
This is the most important function you need to implement in this task. This function has no input parameters. On the other hand, it should return two data. First, the complete Q-value table of all states. And second, the current Q-value estimate of the states you've encountered starting from the first state to the last. It will be used by the automarker to compare the correctness of your implementation against the solution.

### `act()`
This function will be used to choose the actions that your agents will use when faced with a state. It should only return the action that should be taken by the agent at the current state.

### `toStateRepresentation(state)`
You might want to use a different representation compared to the ones provided by the environment. This will provide a problem to the automarker. Therefore, you should implement a function that maps the raw state representation into the the state representation that you are using in your implementation. This function will receive a state and outputs it's value under the representations that you are using in your implementations.

### `setState(state)`
This function will be used to provide the agents you're controlling with the current state information. It will receive the state representation from the environment as an input. On the other hand, this does not need to output anything.

### `setExperience(state, action, reward, status, nextState)`
Once an agent executes an action, it will receive the rewards, status, and next states resulting from that action. Use this method to set these data to prepare your agent to learn using the Monte Carlo update.

### `reset()`
You might want to reset some states of an agent at the beginning of each episode. Use this function to do that. This function does not require any inputs. Additionally, it also does not provide any outputs.

### `setEpsilon(epsilon)`
This function should be used to set the epsilon that you use during training. 
