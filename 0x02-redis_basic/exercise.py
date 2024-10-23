#!/usr/bin/env python3
"""Exercise"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Constructor"""
        self._redis = redis.Redis()

    def store(
            self,
            data: Union[str, bytes, int, float]) -> str:
        """Cache up data"""
        id: str = str(uuid4())
        self._redis.set(id, data)
        return id
