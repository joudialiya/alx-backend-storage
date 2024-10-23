#!/usr/bin/env python3
"""Exercise"""
import redis
import typing
import uuid
import functools


def count_calls(method: typing.Callable) -> typing.Callable:
    """ Count calls Decorator """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """Wraps the crud function to add the count functionality"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Cache class """
    def __init__(self) -> None:
        """ The constructor of the cahing class"""
        self._redis = redis.Redis()

    @count_calls
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """ Cache up data with random key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: typing.Optional[typing.Callable] = None
            ) -> typing.Union[str, bytes, int, float]:
        """Retrieve data"""
        result = self._redis.get(key)
        if result is None:
            return None
        return fn(result) if fn is not None else result

    def get_str(self, key: str) -> str:
        """Retrieve str"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve int"""
        return self.get(key, lambda d: int(d))
