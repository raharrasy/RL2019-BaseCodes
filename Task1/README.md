# Task 1 - Value Iteration

You are required to implement the Value Iteration algorithm using the codes provided in `BellmanDPBase.py`. In this case, an MDP specifying the reward function and transition distribution of the environments are going to be given in the `MDP.py` file. Your task is to implement the `totalBellmanUpdate()` method in `BellmanDPBase.py` and make a working implementation for a complete update of value iteration.

## Specifications

## 1. Bellman Update Parameters
You have already been provided an explanation of the value iteration algorithm and it's parameters in lectures. In this case, the only parameters are it's discount rate. Fill in the base codes to enable the creation of an object of the `BellmanDPSolver` class by using `BellmanDPSolver(discountRate)`.

## 2. Value Function and Policy Initialization
The result of the initial iterations of the value iteration algorithm depends on the initial values of states and the policies. To allow standardized marking, set the initial values of all states to zero and the policy to be a uniform distribution. Implement these initializations in the `initVs()` function.

## 3. The MDP Specifications
The environment is a gridworld soccer domain with a `5x5` grid size. The trained agents' objective is then to score a goal in this gridworld. However, you will have different probabilities of scoring a goal in different parts of the gridworld. Hence, the agent must learn to move to more advantageous positions to score a goal.

The agent is supported with the capability of executing actions like `MOVE_UP`, `MOVE_DOWN`, `MOVE_LEFT`, `MOVE_RIGHT`, and `SHOOT`. The next states resulting from these actions are not deterministic. Examples of the transition probabilities and the rewards resulting from executing these actions might be seen in the `MDP.py` file. In general, you need to use the reward data and transition probabilities defined in `MDP.py`. During the marking process, we will test your implementation with different dynamics and see whether you implementations matches our solutions.

## 4. Update Results
Implement a single iteration Value Iteration Update inside the `totalBellmanUpdate()` function. First, store your state values and policies in a variable inside your `BellmanDPSolver` class. This function should then return the state values and the policy after a single update. We will check the correctness of you implementation by repeatedly calling `totalBellmanUpdate()` and seeing whether the results match with the solutions or not.

We also require your returns to be in a specific format. For your state values, store the results as a python dictionary which has the state representation as keys and the state values as the value of the corresponding key. As an example, a state value table with all zeros will be represented as :

`{(1, 3): 0, (3, 0): 0, (2, 1): 0, (0, 3): 0, (4, 0): 0, (1, 2): 0, (3, 3): 0, (4, 4): 0, (2, 2): 0, (4, 1): 0, (1, 1): 0, 'OUT': 0, (3, 2): 0, (0, 0): 0, (0, 4): 0, (1, 4): 0, (2, 3): 0, (4, 2): 0, (1, 0): 0, (0, 1): 0, 'GOAL': 0, (3, 1): 0, (2, 4): 0, (2, 0): 0, (4, 3): 0, (3, 4): 0, (0, 2): 0}`

We also require you to output dictionaries for the policy. However, the values are now lists and no longer scalars. This is done since there might be actions which results in the same next state expected values when taken at a certain state. In such cases, we require you to specify all actions following this following order :
..* `"DRIBBLE_UP"`
..* `"DRIBBLE_DOWN"`
..* `"DRIBBLE_LEFT"`
..* `"DRIBBLE_RIGHT"`
..* `"SHOOT"`

As an example, a policy where all states have an optimal action of `"DRIBBLE_UP"` and `"SHOOT"`, except `(1,2)` which optimal action is only `"SHOOT"`, will be represented as :

`{(1, 3): ['DRIBBLE_UP', 'SHOOT'], (3, 0): ['DRIBBLE_UP', 'SHOOT'], (2, 1): ['DRIBBLE_UP', 'SHOOT'], (0, 3): ['DRIBBLE_UP', 'SHOOT'], (4, 0): ['DRIBBLE_UP', 'SHOOT'], (1, 2): ['DRIBBLE_UP'], (3, 3): ['DRIBBLE_UP', 'SHOOT'], (4, 4): ['DRIBBLE_UP', 'SHOOT'], (2, 2): ['DRIBBLE_UP', 'SHOOT'], (4, 1): ['DRIBBLE_UP', 'SHOOT'], (1, 1): ['DRIBBLE_UP', 'SHOOT'], 'OUT': ['DRIBBLE_UP', 'SHOOT'], (3, 2): ['DRIBBLE_UP', 'SHOOT'], (0, 0): ['DRIBBLE_UP', 'SHOOT'], (0, 4): ['DRIBBLE_UP', 'SHOOT'], (1, 4): ['DRIBBLE_UP', 'SHOOT'], (2, 3): ['DRIBBLE_UP', 'SHOOT'], (4, 2): ['DRIBBLE_UP', 'SHOOT'], (1, 0): ['DRIBBLE_UP', 'SHOOT'], (0, 1): ['DRIBBLE_UP', 'SHOOT'], 'GOAL': ['DRIBBLE_UP', 'SHOOT'], (3, 1): ['DRIBBLE_UP', 'SHOOT'], (2, 4): ['DRIBBLE_UP', 'SHOOT'], (2, 0): ['DRIBBLE_UP', 'SHOOT'], (4, 3): ['DRIBBLE_UP', 'SHOOT'], (3, 4): ['DRIBBLE_UP', 'SHOOT'], (0, 2): ['DRIBBLE_UP', 'SHOOT']}`

