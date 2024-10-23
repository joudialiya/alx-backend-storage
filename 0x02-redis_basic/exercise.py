#!/usr/bin/env python3
"""Exercise"""
import redis
import typing
import uuid


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Constructor"""
        self._redis: redis.Redis = redis.Redis()

    def store(
            self,
            data: typing.Union[str, bytes, int, float]) -> str:
        """Cache up data"""
        id: str = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
