# Exercise 2 - Q-Learning, SARSA, and first-visit MC control with soft policies

In this exercise, your task is to implement an attacking agent in the discretized Half Field Offense (HFO) domain. Your agent will be controlled using Q-Learning (**Section 6.5 of the book**), SARSA (**Section 6.4 of the book**), and first visit Monte Carlo control with soft policies (**Algorithm in page 101 of the book**). 

Just like in Exercise 1, the environment is a gridworld where each position is associated with a probability of scoring a goal. Additionally, defending players are positioned in parts of the environment and act as obstacles. Episodes always end when the agent selects the **KICK** action. If an agent manages to score a goal in an episode, the agent receives a reward of **+1**. The agent will be punished with a penalty if it moves into a grid location occupied by a defending player. The position of defending players will not change during the course of each episode. 

Full codes for the discretized HFO domain can be found in the `DiscreteHFO` folder. In particular, `DiscreteHFO/HFOAttackingPlayer.py` contains the implementation of the interface between the HFO domain and your agent controller. 

## Setup and Requirements

A lot of students have noted that they ran into installation problems on DICE. As an alternative to DICE, you can also install HFO on the MLP cluster. However, if trouble persists, we encourage students to contact the demonstrators directly or visit the demonstration sessions that are going to be held in the following weeks. We do not provide any guarantee that this will work on your personal computers, but we guarantee that it will work in either DICE or the MLP clusters and will help troubleshoot any problems encountered for installing in DICE or the MLP clusters.

To access DICE or the MLP servers from your personal computers, use the following commands for DICE:
```
ssh -X <UUN>@student.ssh.inf.ed.ac.uk
ssh -X student.compute
```

Or use these commands for working in the MLP clusters:
```
ssh -X <UUN>@student.ssh.inf.ed.ac.uk
ssh -X <mlp1/mlp2>
```

The **-X** flags are important if you want to display the visualizations in your local computer. Otherwise, you can actually remove them when connecting to the clusters. 

All the necessary dependencies of HFO, like **qt4** and **boost** have already been installed in DICE and the MLP clusters. To install the HFO environment, create a virtual environment that contains all the packages that you might need for running the task:

```
mkvirtualenv --python=`which python3` <your env name>
workon <your env name>
# Run this to install all the packages you might find necessary
pip install <packages>
```

Then, you just need to clone the HFO environment using the following command:
```
git clone https://github.com/raharrasy/HFO.git
```

Afterwards, follow the full installation intructions and documentation of this environment. This can be seen [in this repository](https://github.com/raharrasy/HFO). Finally, after installing the environment, clone this repository into the `example` directory in the `HFO` folder using the following commands:

```
cd HFO/example
git clone https://github.com/raharrasy/RL2019-BaseCodes.git
```

## Working on Task 2

### Minimum working example
A minimum working example of how the agent interacts with the environment is provided in `RandomAgentExample/DiscretizedRandomAttackingController.py`

To start this task, you must first understand how to connect your agent to the HFO server. In the working example, this is provided in line 19-20. At the beginning of each episode, the agent will then need to get an initial state from the environment. An example on how to do this is provided in line 26.

You then need to implement algorithms that choose actions to take given a certain state. Then, pass the selected action through the provided `step` function in line 30. As a response, the environment will respond by providing your agent with the next state, reward, and episode completion information. 

To run your implementation and display the environment through the visualizer, do the following steps:

```
# Move to the example directory in your HFO folder and clone the latest code base
cd HFO/example
git clone https://github.com/raharrasy/RL2019-BaseCodes.git
# Move to the directory that contains the code base for the algorithm you'd like to implement
cd RL2019-BaseCodes/Exercise2/<Algorithm Code Base Directory>
cp * ..
cd ..
./<Caller for desired algorithm>.sh
```  

## Marking
Marking will be based on the correctness of your implementations and the performance of your agents. 

To examine the correctness of the implementations, we will require you to implement functions that output specific values related to the algorithm being implemented. To find these functions and what they are supposed to output, refer to the README files inside each specific algorithm that you are supposed to implement. Additionally, we've also provided a small section of code in the **main** functions in each python files to provide information on how the functions are supposed to interact. You **must implement your agents such that the sequence of commands in the main function can train your agents**.

On the **performance marking**, we will do several experiments under the same MDP where we **run the agents for 5000 episodes** using commands that are similar to what has been provided in the **main functions**. **In these experiments, we guarantee that the size of the grid will be 6x5, there will only be a single defender, and the location of the defender does not change across the 5000 episodes**. Additionally, we also guarantee that **in each experiment we will store the performance of your agents in episodes that are divisible by 500 and average this value across experiments. We will then make a plot of the agent performance and compare it with our solutions. In 5000 episodes, given good hyperparameter settings, your agents should be able to reach performance that is close to optimal.**

## Additional Information

### Implemented Files (**Contains functions to be implemented**)
1. `QLearning/QLearningBase.py`
2. `MonteCarlo/MonteCarloBase.py`
3. `SARSA/SARSABase.py`

### Environment Files (**Should not be modified**)
1. `DiscreteHFO/HFOAttackingPlayer.py`
   - File to establish connections with HFO and preprocess state representations gathered from the HFO domain.
2. `DiscreteHFO/HFODefendingPlayer.py`
   - File to control defending player inside the HFO environment. 
3. `DiscreteHFO/HFOGoalkeepingPlayer.py`
   - File to control Goalkeeper inside the HFO environment. HFO environment cannot run without a goalkeeper. 
4. `DiscreteHFO/DiscretizedDefendingPlayer.py`
   - File to initialize the defending player.
5. `DiscreteHFO/Goalkeeper.py`
   - File to initialize the Goalkeeper.
   
### Caller Files (**Can be modified, adapt to your existing directories if necessary**)
1. `QLearning/QLearningAgent.sh`
   - This file runs all the necessary files to initialize a discrete HFO domain and run a Q-Learning agent.
2. `SARSA/SARSAAgent.sh`
   - This file runs all the necessary files to initialize a discrete HFO domain and run a SARSA agent.
3. `MonteCarlo/MonteCarlo.sh`
   - This file runs all the necessary files to initialize a discrete HFO domain and run a Monte Carlo agent.

## Environment Details
   
### State Space
The environment is modelled as a 6x5 grid. The grid cell with `(0,0)` coordinate is located in the top left part of the field. At each timestep, the agent will be given a state representation, in the form of a list, which has information on the defending players' location and the agent's own location on the grid. The first item in the list is the agent's location and the rest are the location of the defending players. 

The location of the goal is not modelled inside the grid. Therefore, agents cannot dribble into the goal and must rely on the `KICK` action to score goals. 

### Action Spaces
Agents are equipped with a set of discrete actions. To move to adjacent grids, agents can use the `DRIBBLE_UP`,`DRIBBLE_DOWN`,`DRIBBLE_LEFT`, and `DRIBBLE_RIGHT` actions. Additionally, the `KICK` action enables the agents to shoot the ball toward the goal. 

### Reward Functions
Agents only receive non-zero rewards at the completion of each episode. In this case, a goal will result in a reward of **+1**. However, occupying the same grid as defending players will result in a penalty.

### Environment Dynamics
Environment transitions resulting from the actions are stochastic. For the dribbling actions, there will be a small probability for agents to end up dribbling into an adjacent (but wrong) grid. There is also the possibility of agent's kicks going wayward from the goal after executing the `KICK` action. This probability of kicking the ball depends on the location in the grid that the agent executes the `KICK` action from.

## Status
Status are integers that denote certain terminal events in the game. It will always be 0 when the agents are in the middle of a game. Other numbers might denote different events like a goal successfully scored, ball kicked out of bounds, or episodes running out of time. Full information of the possible status values for the HFO environment can be seen at `HFO/bin/HFO` script inside the HFO codes given in the original HFO repository.

