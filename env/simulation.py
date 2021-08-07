class Config:
    def __init__(self):
        return


class Simulation:
    def __init__(self):
        self.env = InsulinControl()
        return

    def step(self, action):
        observation, reward, done = self.env.step(action)
        return observation, reward, done

    def legal_actions(self):
        legal_actions = self.env.legal_actions()
        return legal_actions

    def reset(self):
        return self.env.reset()

    def render(self):
        self.env.render()


class InsulinControl:
    def __init__(self):
        return

    def step(self, action):
        observation = None
        reward = None
        done = None
        return observation, reward, done

    def legal_actions(self):
        legal_actions = None
        return legal_actions
