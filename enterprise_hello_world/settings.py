from typing import Any, Callable, Set
from pydantic import (BaseModel, Field)
from pydantic_settings import BaseSettings, SettingsConfigDict

class SubModel(BaseModel):
    foo: str = 'bar'
    apple: int = 1

class Settings(BaseSettings):
    hello_world_count: int = Field(default=10, validation_alias='HELLO_WORLD_COUNT')

    # to override more_settings:
    # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
    more_settings: SubModel = SubModel()

    model_config = SettingsConfigDict(env_prefix='HELLO_WORLD_')
