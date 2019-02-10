# Exercise 4 - Independent Q-Learning, Joint Action Learning, and WoLF-PHC for discrete multiagent RL.

In this task, you are required to implement an attacking agent in a discretized soccer domain. We move away from HFO for this task and just use a simple discretized domain. These implemented agents will be controlled using the Independent Q-Learning (**Like Exercise 2, each agent independently using Q-Learning without sharing information with other agents**), Joint action learning with opponent modelling (see the readme in the "JointActionLearner" folder for details), and WoLF-PHC as described in [**Bowling and Veloso, 2001**](http://www.cs.cmu.edu/~mmv/papers/01ijcai-mike.pdf). 

Just like in Exercise 2, each position in the gridworld is associated with a probability of scoring goals. Also, defending NPCs are positioned in parts of the environment and acts as obstacles. Ball carrying agents will also be punished with a penalty if it moves into a grid occupied by a defensive NPC. The position of defense NPCs will not change during the course of each episode.

However, unlike Exercise 2, the team of agents will only receive a reward of **+1** if one of the members of the team covers the opponent by moving into the sme grid location as the opponent while the kick is converted into a goal. As a result, an optimal policy for this domain should be one where an agent covers the opponent while the other moves to an advantageous location and scores a goal. This requires some coordination between both of the trained agents.

Full codes for the discretized Multiagent RL domain can be found in the `DiscreteMARLUtils` folder. In particular, `DiscreteMARLUtils/Environment.py` contains the implementation of the interface between the HFO domain and your agent controller. You must then implement algorithms that choose actions to take given a certain state, and pass it through the provided `act` method. This environment will respond by providing your agents with the next state, reward, and episode completion information. 

## Implemented Files (**Contains functions to be implemented**)
1. `IndependentQLearning/IndependentQLearning.py`
2. `JointActionLearner/JointActionLearnerBase.py`
3. `WolfPHCAgent/WolfPHCBase.py`

## Environment Files (**Should not be modified**)
1. `DiscreteMARLUtils/Environment.py`
   - Specifies the environment for Exercise 4. Mostly similar with Exercise 2, just without any usage of HFO APIs. Also check at the reward functions to see how it's calculated.
2. `DiscreteMARLUtils/Agent.py`
   - Specifies the necessary functions that all agents must have.

## State Space
The environment is modelled as a 5x5 grid. The grid with `(0,0)` coordinate is located in the top left part of the field. At each timestep, agents will be given a state representation, in form of a list, which has information on their teammates', defensive NPCs' and their own location on the grid. 

Also, the location of the goal is not modelled inside the grid. Therefore, agents cannot dribble into the goal and must rely on the `KICK` action to score goals. 

## Action Spaces
Agents are equipped with a set of discrete actions. To move to adjacent grids, agents can use the `DRIBBLE_UP`,`DRIBBLE_DOWN`,`DRIBBLE_LEFT`, and `DRIBBLE_RIGHT` actions. Additionally, the `KICK` action enables the agents to shoot the ball into the goal. 

## Reward Functions
Agents only receive non-zero rewards at the completion of each episodes. In this case, a goal while an agent of the team successfully covers the opponent will result in a reward of **+1**. However, if a ball carrying agent occupies the same grid as opponent agents, it will result in a penalty to both controlled agents.

## Environment Dynamics
Environment transition resulting from the actions are stochastic. For the dribbling related actions, there will be a small probability for agents to end up dribbling into an adjacent (but wrong) grid. There is also some possibility of agents kicks going wayward from the goal after executing the `KICK` action. This probability of kicking the ball depends on the location of the grid that the agent executes the `KICK` action from.

## Implementing Your Own Agents
You are required to implement Independent Q-Learning, Joint Action Learning, and WoLF-PHC. To this end, we've provided you with code snippets which indicates the functions that you should implement. To find the skeleton codes for each algorithm, open the `IndependentQLearning`, `JointActionLearner`, and `WoLFPHCAgent` folders respectively. Further instructions for each task can be found in the markdown files inside the aforementioned folders.

## Dependencies
The `DiscreteMARLUtils/Environment.py` depends on the `pygame` package to visualize the environment. Therefore, if you'd like to get a visualization of your agent, you should install `pygame` using the code below. 
```
conda install -c cogsci pygame
```

Nevertheless, the visualization slows down the execution of the code. Hence, it is not recommended to use the visualizations when training the agent.
