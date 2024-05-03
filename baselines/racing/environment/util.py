from typing import Union, List, Dict
import gymnasium
import yaml
import gymnasium.wrappers as gym_wrappers


def wrap_env(env: gymnasium.Env, wrapper_configs: Union[str, List[Dict]]) -> gymnasium.Env:
    if isinstance(wrapper_configs, str):
        with open(wrapper_configs, 'r') as file:
            wrapper_configs = yaml.safe_load(file)

    def has_modules(name: str, module):
        mod = module
        for m in name.split('.'):
            if not hasattr(mod, m):
                return False
            else:
                mod = getattr(mod, m)
        return True

    def get_cls(name: str, module):
        mod = module
        for name in name.split('.'):
            mod = getattr(mod, name)
        return mod

    for wrapper in wrapper_configs:
        name = wrapper['name']
        if has_modules(name=name, module=wrappers):
            wrapper_cls = get_cls(name=name, module=wrappers)
        elif hasattr(gym_wrappers, name):
            wrapper_cls = getattr(gym_wrappers, name)
        else:
            raise NotImplementedError(f'No wrapper named {name} available.')
        del wrapper['name']
        env = wrapper_cls(env, **wrapper)
    return env