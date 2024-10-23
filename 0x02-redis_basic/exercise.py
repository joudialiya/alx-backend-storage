#!/usr/bin/env python3
"""Exercise"""
import redis
import typing
import uuid


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Constructor"""
        self._redis: redis.Redis = redis.Redis('127.0.0.1', 6379)

    def store(
            self,
            data: typing.Union[str, bytes, int, float]) -> str:
        id: str = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
