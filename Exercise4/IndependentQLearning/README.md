# Exercise 4 - Independent Q-Learning

The instructions for this task are exactly the same as Task 2's Q-Learning instructions. The function that you implement have the same functionality with it's Q-Learning counterpart. The difference between the code provided here and the Q-Learning code in Task 2 only lies in the `__main__` function.

In the `__main__` function of this script, instead of immediately providing the environment with information on the agent's action once it has been chosen, the environment waits until all agents have decided on which action to take (see line 72). Additionally, the environment provides an observation for every agent instead of only for one agent once `step()` is called. However, in this task, the observations assigned to each agent are the same. To see how agents must process the group observation to retreive its individual observation, see line 69 in `IndependentQLearningAgent.py`

### Training process
To see how your implemented functions interact with each other to train the agent, check the `__main__` function inside `QLearningBase.py`. Make sure that you can successfully train your agent using the **exact same** codes inside `__main__` to ensure that your implementations are correct. This snippet of code used in `__main__` is also going to be used in the marking process.

## Marking details
### Performance marking
Using similar codes as what you've seen in `__main__`, we are going to run your agent on a randomly sampled environment and compare its performance to our solution. Performance is then measured by running an experiment of 50000 episodes using your implementation. We then divide the sequence of episodes into groups of consecutive 1000 episodes and average the reward of the agent on these groups for evaluation. 

To provide a good performance, ensure that you carefully schedule your hyperparameters so the agents can learn to coordinate in 50000 episodes. Use `computeHyperparameters()` to specify a hyperparameter scheduling scheme.

### Unit test marking
We compare the results of updates from `learn()`. Just like in Q-Learning, this function should return the difference between the value of the updated state-action pair after and before the update (Q(s_t,a_t)(t+1) - Q(s_t,a_t)(t)).

As an example, assume that both agents in the environment observed the following experiences,

```
Timestep, State, Agent 1 Action, Agent 2 Action, Agent 1 Reward, Agent 2 Reward, Next State
1, [[[1,1],[1,3]], [1,3] ,[2,3]], MOVE_UP, MOVE_RIGHT, -0.4, -0.4, [[[1,0],[2,3]], [2,3] ,[2,3]]
2, [[[1,0],[2,3]], [2,3] ,[2,3]], MOVE_DOWN, MOVE_LEFT, 0.0, 0.0, [[[1,1],[1,3]], [1,3] ,[2,3]]
3. [[[1,1],[1,3]], [1,3] ,[2,3]], NO_OP, KICK, 0.0, 0.0, ["GOAL", "GOAL"]
```

Then, the outputs of learn should be something like :
```
Timestep, Agent 1 learn() output, Agent 2 learn() output
1, Change in Q<[[[1,1],[1,3]], [1,3] ,[2,3]], MOVE_UP>, Change in Q<[[[1,1],[1,3]], [1,3] ,[2,3]], MOVE_RIGHT>
2, Change in Q<[[[1,0],[2,3]], [2,3] ,[2,3]], MOVE_DOWN>, Change in Q<[[[1,0],[2,3]], [2,3] ,[2,3]], MOVE_LEFT>
3, Change in Q<[[[1,1],[1,3]], [1,3] ,[2,3]], NO_OP>, Change in Q<[[[1,1],[1,3]], [1,3] ,[2,3]], KICK>
```
which in this case, should be :
```
Timestep, Agent 1 learn() output, Agent 2 learn() output
1, -0.04, -0.04 
2, 0.0, 0.0
3, 0.0, 0.0
```
