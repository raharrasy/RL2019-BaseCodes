# Task 3 - Independent Q-Learning

The instructions for this task is exactly the same with Task 2's Q-Learning instructions. The function that you implement have the same functionality with it's Q-Learning counterpart. The difference between the code provided here and the Q-Learning code in Task 2 only lies in the `__main__` function.

In the `__main__` function of this script, instead of immediately providing the environment with information on agent's actions once it has been chosen, the environment waits until all agents have decided on which action to take (see line 52). Additionally, the agent provides an observation for every agent instead of only for one agent once `step()` is called. Although in this task, the observation assigned to each agent is the same. To see how agent's must process the group observation to retreive it's individual observation, see line 49 in `IndependentQLearningAgent.py`
