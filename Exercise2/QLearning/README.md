# Exercise 2 - Q-Learning Methods

You are required to implement the Q-Learning algorithm using the codes provided in `QLearningBase.py`. Before you proceed, install the HFO Domain first by following the necessary steps outlined in `Exercise2/README.md`. Your task is to extend `QLearningBase.py` by implementing functions that have yet been implemented.

## Specifications
### Automarking requirements
To ensure that your codes can be used by the marking script, ensure that all the necessary functions have been implemented. To check whether these implementations are correct, use the code snippet given in `__main__` to test your implementation. This code snippet provides an outline of how your implemented functions will interact to train a Q-Learning agent. If you just modify the number of episodes and the hyperparameters for training, you can use this code to train a Q-Learning agent.

Additionally, **ensure that the initial Q-Values of all state-action pairs are initialized to zero prior to training**. Although you can technically use any initialization value for Q-Learning, we require this as a means for unit testing your implementations.

### Implemented Functions
#### `__init__(self, learningRate, discountFactor, epsilon)`
This init function should initialize all the necessary parameters for training a Q-Learning Agent. This includes the learning rate, discount factor, and the epsilon value (if you use an epsilon greedy exploration strategy). This function will only be called once at the very beginning when you initialize agents for training.

#### `learn()` - Used in Automarking
This is the most important function you need to implement in this task. This function has no input parameters. On the other hand, this method **must** return a single scalar that specifies the change **(value after update subtracted by value before update)** in updated state-action value after you've trained your agents using Q-Learning's update. It will be used by the automarker to compare the correctness of your implementation against the solution. **This function has the same functionality as line 8 in the books' Q-Learning pseudocode**

#### `act()`
This function will be used to choose the actions that your agents will use when faced with a state. It should only return the action that should be taken by the agent at the current state. In general, this will have the same functionality as **line 6 in the books' Q-Learning pseudocode.**

#### `toStateRepresentation(state)`
You might want to use a different representation compared to the ones provided by the environment. This will provide a problem to the automarker. Therefore, you should implement a function that maps the raw state representation into the the state representation that you are using in your implementation. This function will receive a state and outputs it's value under the representations that you are using in your implementations. Additionally, this state representation **must be able to be used as keys of a python dictionary** since the marking tools will use this to check the correctness of your algorithm.

#### `setState(state)`
This function will be used to provide the agents you're controlling with the current state information. It will receive the state representation from the environment as an input. On the other hand, this does not need to output anything. **This is generally equivalent to line 9 of the Q-Learning pseudocode given in the book.**

#### `setExperience(state, action, reward, status, nextState)`
Once an agent executes an action, it will receive the rewards, status, and next states resulting from that action. Use this method to set these data to prepare your agent to learn using the Q-Learning update. **This is generally equivalent to line 7 of the Q-Learning pseudocode given in the book**

#### `reset()`
You might want to reset some states of an agent at the beginning of each episode. Use this function to do that. This function does not require any inputs. Additionally, it also does not provide any outputs.

#### `setLearningRate(learningRate)` and `setEpsilon(epsilon)`
This function should be used to set the learning rate and the epsilon (if you are using epsilon greedy) that you use during training. 

#### `computeHyperparameters(numTakenActions, episodeNumber)`
This function should return a tuple indicating the learning rate and epsilon used at a certain timestep. This allows you to schedule the values of your hyperparameters and change it midway of training.

### Training process
To see how your implemented function interact with each other to train the agent, check the `__main__` function inside `QLearningBase.py`. Make sure that you can successfully train your agent using the codes inside `__main__` to ensure that your implementations are correct. A similar sequence of commands with those provded in`__main__` is also going to be used in the marking process.

## Marking details
### Performance marking
Using similar codes as what you've seen in `__main__`, we are going to run your agent on a randomly sampled MDP and compare it's performance to our solution. For details on the experiment, refer to the **Marking** section in Exercise 2's README.

### Unit test marking
We compare the results of updates from `learn()`. This function should return the difference between the value of the updated state-action pair after and before the update. (Q(s_t,a_t)(t+1) - Q(s_t,a_t)(t)) 

As an example, let's say that an agent is exposed to the following sequence of experience:
```
Timestep Number, State, Action, Reward, Next State
1, ((1,1),(2,1)), MOVE_RIGHT, -0.4, ((2,1),(2,1))
2, ((2,1),(2,1)), MOVE_LEFT, 0.0, ((1,1),(2,1))
3, ((1,1),(2,1)), KICK, 1.0, GOAL
```

Assuming an initial value of 0 for each state-action pair, a learning rate of 0.1 and a discount rate of 1, these should be the outputs of the learn functions at the end of each timestep :

```
Timestep Number, learn Output
1, -0.04 (Calculate the difference in value of < ((1,1),(2,1)), MOVE_RIGHT > before and after update )
2, 0.0 (Calculate the difference in value of < ((2,1),(2,1)), MOVE_LEFT > before and after update )
3, 0.1 (Calculate the difference in value of < ((1,1),(2,1)), KICK > before and after update )
```
