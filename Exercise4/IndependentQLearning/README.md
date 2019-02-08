# Exercise 4 - Independent Q-Learning

The instructions for this task is exactly the same with Task 2's Q-Learning instructions. The function that you implement have the same functionality with it's Q-Learning counterpart. The difference between the code provided here and the Q-Learning code in Task 2 only lies in the `__main__` function.

In the `__main__` function of this script, instead of immediately providing the environment with information on agent's actions once it has been chosen, the environment waits until all agents have decided on which action to take (see line 52). Additionally, the agent provides an observation for every agent instead of only for one agent once `step()` is called. Although in this task, the observation assigned to each agent is the same. To see how agent's must process the group observation to retreive it's individual observation, see line 49 in `IndependentQLearningAgent.py`

### Training process
To see how your implemented function interact with each other to train the agent, check the `__main__` function inside `QLearningBase.py`. Make sure that you can successfully train your agent using the **exact same** codes inside `__main__` to ensure that your implementations are correct. This snippet of code used in `__main__` is also going to be used in the marking process.

## Marking details
### Performance marking
Using similar codes as what you've seen in `__main__`, we are going to run your agent on a randomly sampled environment and compare it's performance to our solution. Performance is measured by running an experiment using your implementation. We then divide the sequence of episodes into groups of consecutive episodes and average the reward of the agent on these groups.

### Unit test marking
We compare the results of updates from `learn()`. Just like in Q-Learning, this function should return the difference between the value of the updated state-action pair after and before the update (Q(s_t,a_t)(t+1) - Q(s_t,a_t)(t)).
