class Script:

    def __init__(self):
        self._actions = {}

    def add_action(self,actionName,action):
        if not actionName in self._actions.keys():
            self._actions[actionName] = []
        
        if not action in self._actions[actionName]:
            self._actions[actionName].append(action)

    def get_action(self,actionName):
        return self._actions[actionName]