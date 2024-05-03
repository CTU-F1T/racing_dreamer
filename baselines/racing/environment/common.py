import gymnasium
from gymnasium import Wrapper


class Vectorized(Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self.observation_space = env.observation_space.spaces[0]
        self.action_space = env.action_space.spaces[0]

    def step(self, action):
        obs, reward, done, info = self.env.step([action])
        return obs[0], reward[0], done[0], info[0]

    def reset(self, **kwargs):
        obs = self.env.reset(**kwargs)
        return obs[0]

    def render(self, mode='human', agent: str = None, **kwargs):
        images = self.env.render()
        return images[0]

class FixedResetMode(gymnasium.Wrapper):
    def __init__(self, env, mode: str):
        super().__init__(env)
        self._mode = mode

    def reset(self, **kwargs):
        # kwargs['options'] = {"mode": self._mode}
        return self.env.reset(**kwargs)

class InfoToObservation(gymnasium.Wrapper):
    def __init__(self, env):
        super().__init__(env)

    def step(self, action):
        obs, reward, done, truncated, info = super().step(action)
        for k, v in info.items():
            obs[f'info_{k}'] = v
        return obs, reward, done, truncated, info
