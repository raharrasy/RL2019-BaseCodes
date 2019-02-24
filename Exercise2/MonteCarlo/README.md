# Exercise 2 - On-Policy First Visit Monte Carlo Control

You are required to implement the On-Policy First Visit Monte Carlo Control with epsilon-soft policies using the codes provided in `MonteCarloBase.py`. Before you proceed, install the HFO Domain first by following the necessary steps outlined in Task2/README.md. Your task is to extend `MonteCarloBase.py` by implementing functions that have yet been implemented.

## Specifications
### Automarking requirements
To ensure that your codes can be used by the marking script, ensure that all the necessary functions have been implemented. To check whether these implementations are correct, you can use the code snippet given in `__main__` to test your implementation. This code snippet gives an outline on how your implemented functions will interact to train a Monte Carlo agent. If you just add some code to modify number of episodes and the hyperparameters for training, you can use this code to train a Monte Carlo agent.

### Implemented Functions
#### `__init__(self, discountFactor, epsilon)`
This init function should initialize all the necessary parameters for training a Monte Carlo Agent. This includes the discount factor and the epsilon value. This function will only be called once at the very beginning when you initialize agents for training.

Additionally, ensure that the initial Q-Values of all state-action pairs are initialized to zero prior to training. Although you can technically use any initialization value for this method, we require this as a means for unit testing your implementations.

#### `learn()` - Used in Automarking
This is the most important function you need to implement in this task. This function has no input parameters. On the other hand, it should return **a tuple of two entries**. The first entry is the **complete Q-value table of all states**. The second entry is the **Q-value estimate after update of the states you've encountered in the episode ordered by their first time appearance in the episode**.

It will be used by the automarker to compare the correctness of your implementation against the solution. 

In general, this function has **similar functionality as line 9 - 16 of the pseudocode presented in the book** 

#### `act()`
This function will be used to choose the actions that your agents will use when faced with a state. It should only return the action that should be taken by the agent at the current state. In general, this function has **similar functionality as line 7 of the pseudocode presented in the book** 

#### `toStateRepresentation(state)`
You might want to use a different representation compared to the ones provided by the environment. This will provide a problem to the automarker. Therefore, you should implement a function that maps the raw state representation into the the state representation that you are using in your implementation. This function will receive a state and outputs it's value under the representations that you are using in your implementation.  Additionally, this state representation **must be able to be used as keys of a python dictionary** since the marking tools will use this to check the correctness of your algorithm. 

#### `setState(state)`
This function will be used to provide the agents you're controlling with the current state information. It will receive the state representation from the environment as an input. On the other hand, this does not need to output anything.

#### `setExperience(state, action, reward, status, nextState)`
Once an agent executes an action, it will receive the rewards, status, and next states resulting from that action. Use this method to set these data to prepare your agent to learn using the Monte Carlo update.

#### `reset()`
You might want to reset some states of an agent at the beginning of each episode. Use this function to do that. This function does not require any inputs. Additionally, it also does not provide any outputs.

#### `setEpsilon(epsilon)`
This function should be used to set the epsilon that you use during training. 

#### `computeHyperparameters(numTakenActions, episodeNumber)`
This function should return a tuple indicating the epsilon used at a certain timestep. This allows you to schedule the values of your hyperparameters and change it mid-training.

### Training process
To see how your implemented function interact with each other to train the agent, check the `__main__` function inside `MonteCarloBase.py`. Make sure that you can successfully train your agent using the **exact same** codes inside `__main__` to ensure that your implementations are correct. This snippet of code used in `__main__` is also going to be used in the marking process.

## Marking details
### Performance marking
Using similar codes as what you've seen in `__main__`, we are going to run your agent on a randomly sampled MDP and compare it's performance to our solution. For details on the experiment, refer to the **Marking** section in Exercise 2's README.

### Unit test marking
We compare the results of updates from `learn()`. This function should return  **a tuple of two entries**. The first entry is the **complete Q-value table of all states**. The second entry is the **Q-value estimate after update of the state-action pairs you've encountered in the episode ordered by their first time appearance in the episode**. We will only use the second entry for automarking.

As an example, let's say that an agent is exposed to the following sequence of experience:
```
Episode 1
Timestep Number, State, Action, Reward, Next State
1, ((1,1),(2,1)), MOVE_RIGHT, -0.4, ((2,1),(2,1))
2, ((2,1),(2,1)), MOVE_LEFT, 0.0, ((1,1),(2,1))
3, ((1,1),(2,1)), MOVE_RIGHT, 0.0, ((0,1),(2,1))
4, ((0,1),(2,1)), MOVE_RIGHT, 0.0, OUT_OF_TIME

Episode 2
Timestep Number, State, Action, Reward, Next State
1, ((1,1),(2,1)), MOVE_RIGHT, 0.0, ((0,1),(2,1))
2, ((0,1),(2,1)), MOVE_LEFT, 0.0, ((1,1),(2,1))
3, ((1,1),(2,1)), MOVE_RIGHT, 0.0, ((0,1),(2,1))
4, ((0,1),(2,1)), MOVE_RIGHT, 0.0, OUT_OF_TIME
```

Assuming an initial value of 0 for each state-action pair and a discount rate of 1, these should be the outputs of the learn functions at the end of each timestep :

```
Episode, learn() result second entry
1, [-0.4, 0, 0] (Denotes [Q<((1,1),(2,1)), MOVE_RIGHT>, Q<((2,1),(2,1)), MOVE_LEFT>, Q<((0,1),(2,1)), MOVE_RIGHT>] after training)
2, [-0.2, 0, 0] (Denotes [Q<((1,1),(2,1)), MOVE_RIGHT>, Q<((0,1),(2,1)), MOVE_LEFT>, Q<((0,1),(2,1)), MOVE_RIGHT>] after training)
```
