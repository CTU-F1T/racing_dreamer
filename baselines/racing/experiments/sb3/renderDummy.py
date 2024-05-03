import gymnasium
import numpy as np

from typing import Any, Callable, Dict, List, Optional, Sequence, Type
from stable_baselines3.common.vec_env import VecEnv, DummyVecEnv


class RenderDummyVecEnv(DummyVecEnv):

    def render(self, mode: Optional[str] = None) -> Optional[np.ndarray]:
        """
        Gym environment rendering. If there are multiple environments then
        they are tiled together in one image via ``BaseVecEnv.render()``.

        :param mode: The rendering type.
        """
        return self.envs[0].render()
