import numpy as np
import pathlib
from models.racing_agent import Agent

class RacingAgent(Agent):

    def __init__(self, algorithm: str, checkpoint_path: pathlib.Path):
        if algorithm == 'ppo':
            from stable_baselines3.ppo import MlpPolicy
        elif algorithm == 'sac':
            from stable_baselines3.sac import MlpPolicy
        elif algorithm == 'td3':
            from stable_baselines3.td3 import MlpPolicy
        else:
            raise NotImplementedError
        policy = MlpPolicy.load(checkpoint_path)
        self._model = policy

    def action(self, observation, state=None) -> np.ndarray:
        action, _ = self._model.predict(observation['lidar'], state, deterministic=True)

        dict_action = {'motor': action[0], 'steering': action[1]}
        return dict_action, state

if __name__ == '__main__':
    agent = RacingAgent(algorithm='td3', checkpoint_path='best_model_td3.zip')
    obs = np.ones(shape=(1080,))
    action = agent.action(obs)
    print()
