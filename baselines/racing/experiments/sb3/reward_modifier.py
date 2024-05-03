"""Wrapper for transforming the reward."""
from typing import Callable

import gymnasium
from gymnasium import Wrapper
# from time import sleep, time


class RewardModifier(Wrapper):

    last_action = 2
    static_steps = 0
    speed_penalty = 0
    breaking_penalty = 0
    stop_penalty = 0
    static_penalty = 0
    base_reward = 0
    # last_time = time()
    # counter = 3

    def step(self, action):
        """Modifies the reward using :meth:`self.reward` after the environment :meth:`env.step`."""
        # sleep(0.0005)
        observation, reward, done, truncated, info = self.env.step(action)
        # sleep(0.0005)
        # print(action['motor'])
        self.base_reward += reward
        reward -= 0.001
        self.speed_penalty -= 0.001
        if action['motor'] < -0.8:
            reward -= 0.01
            self.breaking_penalty -= 0.01
        if action['motor'] < -0.85 and abs(action['motor'] - self.last_action) < 0.05:
            reward -= 0.5
            self.stop_penalty -= 0.5
            self.static_steps += 1
        self.last_action = action['motor'][0]

        if self.static_steps > 20:
            reward -= 10
            self.static_penalty -= 10
            done = True

        # self.counter += 1
        # if self.counter >= 4:
        #     # sleep(0.005)
        #     self.counter = 0
        # print(time() - self.last_time)
        # self.last_time = time()
        return observation, reward, done, truncated, info

    def reset(self, **kwargs):
        """Resets the environment with kwargs."""
        # print("Penalties:\n speed: ", self.speed_penalty, ",\n breaking: ", self.breaking_penalty, ",\n stop: ", self.stop_penalty, ",\n static: ", self.static_penalty, ",\n base: ", self.base_reward)
        self.last_action = 2
        self.static_steps = 0
        self.speed_penalty = 0
        self.breaking_penalty = 0
        self.stop_penalty = 0
        self.static_penalty = 0
        self.base_reward = 0
        # print("Reward Modifier - Reset - reset")
        return self.env.reset(**kwargs)
