# Exercise 2 - Q-Learning, SARSA, and first-visit MC control with soft policies

In this exercise, you are required to implement an attacking agent in the discretized Half Field Offense (HFO) domain. These agents will be controlled using the Q-Learning (**Section 6.5 of the book**), SARSA (**Section 6.4 of the book**), and first visit Monte Carlo control for soft policies (**Algorithm in page 101 of the book**). Just like in Exercise 1, each position in the gridworld is associated with a probability of scoring goals. Also, defending NPCs are positioned in parts of the environment and acts as obstacles. If an agent manages to score a goal in an episode, the agent receives a reward of **+1** and the episode ends. Agents will also be punished with a penalty if it moves into a grid occupied by a defensive NPC. The position of defense NPCs will not change during the course of each episode. 

Full codes for the discretized HFO domain can be found in the `DiscreteHFO` folder. In particular, `DiscreteHFO/HFOAttackingPlayer.py` contains the implementation of the interface between the HFO domain and your agent controller. You must then implement algorithms that choose actions to take given a certain state, and pass it through the provided `act` method. This environment will respond by providing your agent with the next state, reward, and episode completion information. 

To get an example of the usage of this DiscreteHFO domain, you can see an example code for a uniformly random agent in the `RandomAgentExample` folder.

## Implemented Files (**Contains functions to be implemented**)
1. `QLearning/QLearningBase.py`
2. `MonteCarlo/MonteCarloBase.py`
3. `SARSA/SARSABase.py`

## Environment Files (**Should not be modified**)
1. `DiscreteHFO/HFOAttackingPlayer.py`
   - File to establish connections with HFO and preprocess state representations gathered from the HFO domain.
2. `DiscreteHFO/HFODefendingPlayer.py`
   - File to control defending NPCs inside the HFO environment. 
3. `DiscreteHFO/HFOGoalkeepingPlayer.py`
   - File to control Goalkeeping NPCs inside the HFO environment. HFO environment cannot run without a goalkeeper. 
4. `DiscreteHFO/DiscretizedDefendingPlayer.py`
   - File to initialize the defending player.
5. `DiscreteHFO/Goalkeeper.py`
   - File to initialize the Goalkeeper.
   
## Caller Files (**Can be modified, adapt to your existing directories if necessary**)
1. `QLearning/QLearningAgent.sh`
   - This file runs all the necessary files to initialize a discrete HFO domain and run a Q-Learning agent.
2. `SARSA/SARSAAgent.sh`
   - This file runs all the necessary files to initialize a discrete HFO domain and run a SARSA agent.
3. `MonteCarlo/MonteCarlo.sh`
   - This file runs all the necessary files to initialize a discrete HFO domain and run a Monte Carlo agent.
   
## State Space
The environment is modelled as a 6x5 grid. The grid with `(0,0)` coordinate is located in the top left part of the field. At each timestep, agents will be given a state representation, in form of a list, which has information on the defensive NPCs and their own location on the grid. The first item in the list is the agent's location and the rest are the location of the opponents. 

Also, the location of the goal is not modelled inside the grid. Therefore, agents cannot dribble into the goal and must rely on the `KICK` action to score goals. 

## Action Spaces
Agents are equipped with a set of discrete actions. To move to adjacent grids, agents can use the `DRIBBLE_UP`,`DRIBBLE_DOWN`,`DRIBBLE_LEFT`, and `DRIBBLE_RIGHT` actions. Additionally, the `KICK` action enables the agents to shoot the ball into the goal. 

## Reward Functions
Agents only receive non-zero rewards at the completion of each episodes. In this case, a goal will result in a reward of **+1**. However, occupying the same grid as opponent agents will result in a penalty.

## Environment Dynamics
Environment transition resulting from the actions are stochastic. For the dribbling related actions, there will be a small probability for agents to end up dribbling into an adjacent (but wrong) grid. There is also some possibility of agents kicks going wayward from the goal after executing the `KICK` action. This probability of kicking the ball depends on the location of the grid that the agent executes the `KICK` action from.

## Implementing Your Own Agents
You are required to implement the Policy Iteration, Q-Learning, SARSA, and first visit Monte Carlo control with soft policies algorithm. To this end, we've provided you with code snippets which indicates the functions that you should implement. To find the skeleton codes for each algorithm, open the `QLearningAgent`, `SARSA`, and `MonteCarlo` folders respectively. Further instructions for each exercise can be found in the markdown files inside the folders.

## Setup and Requirements

The codes can be executed in your own DICE machines. However, you need to first download the necessary packages before running them. In this exercise, you are going to implement an agent in the Half Field Offense (HFO) domain. Full installation intructions and documentation of this environment can be seen [in this repository](https://github.com/raharrasy/HFO). Use the following commands to install the dependencies for HFO in your DICE machines:

```
conda create --name <Environment Name> numpy python=3.5
source activate <Environment Name>
conda install -c anaconda boost
conda install boost
conda install qt=4
```  

Finally, clone this repository into the `example` directory in the `HFO` folder.

## Example
After doing the necessary setup, you can find an example implementation of a discrete random agent inside the `RandomAgentExample` folder. You can find the controller for this random agent in `DiscretizedAttackingController.py`. At each timestep the controller selects an action and pass it through `step` method in line 30. As a response, the environment will return the next state observed by the agent after executing the action, the resulting reward, a flag indicating the end of an episode, and the status of the game. 

To execute the example, copy the files inside `RandomAgentExample` into it's parent directory and run `RandomAgent.sh`. Assuming your current working directory is `Exercise2`. You could also run the base files of other agents using similar commands with file names appropriately replaced to suit the task you're working on.

```
cp RandomAgentExample/* .
./RandomAgent.sh
```

Full information of the possible statuses for the HFO environment can be seen at `HFO/bin/HFO` script inside the HFO codes given in the original HFO repository.

