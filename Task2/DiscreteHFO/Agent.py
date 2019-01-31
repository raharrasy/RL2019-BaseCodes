class Agent(object):
    def __init__(self):
        self.possibleActions = ['DRIBBLE_UP','DRIBBLE_DOWN','DRIBBLE_LEFT','DRIBBLE_RIGHT','KICK']

    def act(self):
        """ Called at each loop iteration to choose and execute an action.
        Returns:
            None
        """
        raise NotImplementedError

    def learn(self):
        """ Called at each loop iteration when the agent is learning. It should
        implement the learning procedure.
        Returns:
            None
        """
        raise NotImplementedError