import numpy as np
from stable_baselines3 import PPO, SAC, TD3
from racing_agent import Agent


class RacingAgent(Agent):

    def __init__(self, algorithm: str, checkpoint_path: str):
        if algorithm == 'ppo':
            from stable_baselines3.ppo import MlpPolicy
        elif algorithm == 'sac':
            from stable_baselines3.sac import MlpPolicy
        elif algorithm == 'td3':
            from stable_baselines3.td3 import MlpPolicy
        else:
            raise NotImplementedError
        print("MODEL LOAD")
        policy = MlpPolicy.load(f'{checkpoint_path}/best_model')
        self._model = policy
        print("MODEL LOADED")

    def action(self, obs, state=None, **kwargs) -> np.ndarray:
        print("ACTION")
        action, _ = self._model.predict(obs['lidar'], state, deterministic=True)
        return action[0], None      # sac/ppo returns action of size (1,2)

if __name__ == '__main__':
    agent = RacingAgent(algorithm='td3', checkpoint_path='best_model_ppo.zip')
    obs = np.ones(shape=(1080,))
    action = agent.action(obs)
    print()