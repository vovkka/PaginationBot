from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    token: str


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path=path)

    return Config(
        token=env.str('TOKEN')
    )
