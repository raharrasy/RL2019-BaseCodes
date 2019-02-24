# Exercise 4 - Independent Q-Learning

The instructions for this task are exactly the same as Task 2's Q-Learning instructions. The function that you implement have the same functionality with it's Q-Learning counterpart. The difference between the code provided here and the Q-Learning code in Task 2 only lies in the `__main__` function.

In the `__main__` function of this script, instead of immediately providing the environment with information on the agent's action once it has been chosen, the environment waits until all agents have decided on which action to take (see line 52). Additionally, the environment provides an observation for every agent instead of only for one agent once `step()` is called. However, in this task, the observations assigned to each agent are the same. To see how agents must process the group observation to retreive its individual observation, see line 49 in `IndependentQLearningAgent.py`

### Training process
To see how your implemented functions interact with each other to train the agent, check the `__main__` function inside `QLearningBase.py`. Make sure that you can successfully train your agent using the **exact same** codes inside `__main__` to ensure that your implementations are correct. This snippet of code used in `__main__` is also going to be used in the marking process.

## Marking details
### Performance marking
Using similar codes as what you've seen in `__main__`, we are going to run your agent on a randomly sampled environment and compare its performance to our solution. Performance is measured by running an experiment using your implementation. We then divide the sequence of episodes into groups of consecutive episodes and average the reward of the agent on these groups.

### Unit test marking
We compare the results of updates from `learn()`. Just like in Q-Learning, this function should return the difference between the value of the updated state-action pair after and before the update (Q(s_t,a_t)(t+1) - Q(s_t,a_t)(t)).
