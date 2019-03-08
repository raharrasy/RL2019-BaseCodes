# Exercise 4  - WoLF-PHC

In this task, you are required to implement the WoLF-PHC algorithm ([**Bowling and Veloso, 2001**](http://www.cs.cmu.edu/~mmv/papers/01ijcai-mike.pdf)). Unlike Q-Learning based algorithms that follow a greedy policy update, this algorithm follows a hill climbing approach to train a stochastic policy for agents. However, just like Q-Learning, it relies on a table of state-action values to calculate the updates to the policy. To get a better description of the algorithm, refer to the following pseudocode.

![WoLF-PHC Algorithm](images/Wolf.png?raw=true)

## Specifications
### Automarking requirements
To ensure that your codes can be used by the marking script, ensure that all the necessary functions have been implemented. To check whether these implementations are correct, you **must** use the code snippet given in `__main__` to test your implementation. This code snippet provides an outline of how your implemented functions will interact to train a team of agents using WoLF-PHC. If you just modify the number of episodes and the hyperparameters for training, you can use this code to train a team of WoLF-PHC agents.

Additionally, **ensure** that the initial Q-Values of all state-action pairs are initialized to **zero** prior to training. Although you can technically use any initialization value for Q-Learning, we require this as a means for unit testing your implementations.

### Implemented Functions
#### `__init__(self, learningRate, discountFactor, winDelta, loseDelta)`
This init function should initialize all the necessary parameters for training a WoLF-PHC Agent. This includes the learning rate, discount factor, and the win and lose learning rate (delta) values. This function will only be called once at the very beginning when you initialize agents for training.

#### `learn()`
Unlike previous tasks, this function will now lesser importance in WoLF-PHC. This function has no input parameters. On the other hand, this method **must** return a single scalar that specifies the change **(value after update subtracted by value before training)** in updated state-action value after you've trained your agents using WoLF-PHC's state-action update rule. It will be used by the automarker to compare the correctness of your implementation against the solution.

#### `calculateAveragePolicyUpdate()`
In WoLF-PHC, you are to store an average of all policies that have been used in a timestep. This policy average will be useful to compute whether the update uses a win or lose learning rate. In this function, provide a working implementation on updates to the average policy. At the end, this function should return the average policy of the agent at the state where the agent is currently in.

#### `calculatePolicyUpdate()`
After calculating the average policy, updates to agents' current policy can be computed based on the average policy and the Q-values stored in the table. Then, a policy hill climbing approach is used to update the current policy. This method should provide working implementation of the policy hill climbing approach to update agents' current policy. In the end, it must return the updated policy of the state where the agent is currently in.

#### `act()`
This function will be used to choose the actions that your agents will use when faced with a state. It should only return the action that should be taken by the agent at the current state.

#### `toStateRepresentation(state)`
You might want to use a different representation compared to the ones provided by the environment. This will provide a problem to the automarker. Therefore, you should implement a function that maps the raw state representation into the the state representation that you are using in your implementation. This function will receive a state and outputs it's value under the representations that you are using in your implementations. Additionally, this state representation **must be able to be used as keys of a python dictionary** since the marking tools will use this to check the correctness of your algorithm.

#### `setState(state)`
This function will be used to provide the agents you're controlling with the current state information. It will receive the state representation from the environment as an input. On the other hand, this does not need to output anything.

#### `setExperience(state, action, reward, status, nextState)`
Once an agent executes an action, it will receive the rewards, status, and next states resulting from that action. Use this method to set these data to prepare your agent to learn using the WoLF-PHC update.

#### `reset()`
You might want to reset some states of an agent at the beginning of each episode. Use this function to do that. This function does not require any inputs. Additionally, it also does not provide any output.

#### `setLearningRate(learningRate)`, `setLoseDelta(loseDelta)` and `setWinDelta(winDelta)`
This function should be used to set the learning rate, winning and losing delta that you use during training. 

#### `computeHyperparameters(numTakenActions, episodeNumber)`
This function should return a tuple indicating the losing delta, winning delta, and learning rate used at a certain timestep. This allows you to schedule the values of your hyperparameters and change it midway of training.

### Training process
To see how your implemented function interact with each other to train the agent, check the `__main__` function inside `WolfPHCAgent.py`. Make sure that you can successfully train your agent using the **exact same** codes inside `__main__` to ensure that your implementations are correct. This snippet of code used in `__main__` is also going to be used in the marking process.

## Marking details
### Performance marking
Using similar codes as what you've seen in `__main__`, we are going to run your agent on a randomly sampled environment and compare it's performance to our solution. Performance is then measured by running an experiment of 50000 episodes using your implementation. We then divide the sequence of episodes into groups of consecutive 1000 episodes and average the reward of the agent on these groups for evaluation. 

### Unit test marking
#### Desired Outputs
We compare the results of updates from `learn()`, `calculateAveragePolicyUpdate()`, and `calculatePolicyUpdate()` for unit testing.

As an example, let's say that the agent is exposed to the following sequence of experience:
```
Timestep, State, Agent 1 Action, Agent 2 Action, Agent 1 Reward, Agent 2 Reward, Next State
1, [[[1,1],[1,3]], [1,3] ,[2,3]], MOVE_UP, MOVE_RIGHT, -0.4, -0.4, [[[1,0],[2,3]], [2,3] ,[2,3]]
2, [[[1,0],[2,3]], [2,3] ,[2,3]], MOVE_DOWN, MOVE_LEFT, 0.0, 0.0, [[[1,1],[1,3]], [1,3] ,[2,3]]
3. [[[1,1],[1,3]], [1,3] ,[2,3]], NO_OP, KICK, 0.0, 0.0, ["GOAL", "GOAL"]
```

Then, the output of `learn()`, `calculateAveragePolicyUpdate()`, and `calculatePolicyUpdate()` should be :
```
Timestep, Agent 1 learn() output, Agent 2 learn() output, Agent 1 calculateAveragePolicyUpdate() output, Agent 2 calculateAveragePolicyUpdate() output, Agent 1 calculatePolicyUpdate() Output, Agent 2 calculatePolicyUpdate() Output
1, Change in Q<[[[1,1],[1,3]], [1,3] ,[2,3]], MOVE_UP>, Change in Q<[[[1,1],[1,3]], [1,3] ,[2,3]], MOVE_RIGHT> 
2, Change in Q<[[[1,0],[2,3]], [2,3] ,[2,3]], MOVE_DOWN>, Change in Q<[[[1,0],[2,3]], [2,3] ,[2,3]], MOVE_LEFT> 
3, Change in Q<[[[1,1],[1,3]], [1,3] ,[2,3]], NO_OP>, Change in Q<[[[1,1],[1,3]], [1,3] ,[2,3]], KICK> 
```

```
Timestep, Agent 1 calculateAveragePolicyUpdate() output, Agent 2 calculateAveragePolicyUpdate() output
1, [p_avg('MOVE_UP'), p_avg('MOVE_DOWN'), p_avg('MOVE_LEFT'), p('MOVE_RIGHT'), p_avg('KICK'), p_avg('NO_OP')] at [[[1,1],[1,3]], [1,3] ,[2,3]] for agent 1, [p_avg('MOVE_UP'), p_avg('MOVE_DOWN'), p_avg('MOVE_LEFT'), p('MOVE_RIGHT'), p_avg('KICK'), p_avg('NO_OP')] at [[[1,1],[1,3]], [1,3] ,[2,3]] for agent 2
2,[p_avg('MOVE_UP'), p_avg('MOVE_DOWN'), p_avg('MOVE_LEFT'), p('MOVE_RIGHT'), p_avg('KICK'), p_avg('NO_OP')] at [[[1,0],[2,3]], [2,3] ,[2,3]] for agent 1, [p_avg('MOVE_UP'), p_avg('MOVE_DOWN'), p_avg('MOVE_LEFT'), p('MOVE_RIGHT'), p_avg('KICK'), p_avg('NO_OP')] at [[[1,0],[2,3]], [2,3] ,[2,3]] for agent 2
3,[p_avg('MOVE_UP'), p_avg('MOVE_DOWN'), p_avg('MOVE_LEFT'), p('MOVE_RIGHT'), p_avg('KICK'), p_avg('NO_OP')] at [[[1,1],[1,3]], [1,3] ,[2,3]] for agent 1, [p_avg('MOVE_UP'), p_avg('MOVE_DOWN'), p_avg('MOVE_LEFT'), p('MOVE_RIGHT'), p_avg('KICK'), p_avg('NO_OP')] at [[[1,1],[1,3]], [1,3] ,[2,3]] for agent 2
```
, and,
```
Timestep, Agent 1 calculatePolicyUpdate() output, Agent 2 calculatePolicyUpdate() output
1, [p('MOVE_UP'), p('MOVE_DOWN'), p('MOVE_LEFT'), p('MOVE_RIGHT'), p_avg('KICK'), p_avg('NO_OP')] at [[[1,1],[1,3]], [1,3] ,[2,3]] for agent 1, [p('MOVE_UP'), p('MOVE_DOWN'), p('MOVE_LEFT'), p('MOVE_RIGHT'), p('KICK'), p('NO_OP')] at [[[1,1],[1,3]], [1,3] ,[2,3]] for agent 2
2,[p('MOVE_UP'), p('MOVE_DOWN'), p('MOVE_LEFT'), p('MOVE_RIGHT'), p('KICK'), p('NO_OP')] at [[[1,0],[2,3]], [2,3] ,[2,3]] for agent 1, [p('MOVE_UP'), p('MOVE_DOWN'), p('MOVE_LEFT'), p('MOVE_RIGHT'), p('KICK'), p('NO_OP')] at [[[1,0],[2,3]], [2,3] ,[2,3]] for agent 2
3,[p('MOVE_UP'), p('MOVE_DOWN'), p('MOVE_LEFT'), p('MOVE_RIGHT'), p('KICK'), p('NO_OP')] at [[[1,1],[1,3]], [1,3] ,[2,3]] for agent 1, [p('MOVE_UP'), p('MOVE_DOWN'), p('MOVE_LEFT'), p('MOVE_RIGHT'), p('KICK'), p('NO_OP')] at [[[1,1],[1,3]], [1,3] ,[2,3]] for agent 2
```

