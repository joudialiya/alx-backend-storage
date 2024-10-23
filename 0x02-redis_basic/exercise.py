#!/usr/bin/env python3
"""Exercise module about decorators and redis"""
import functools
import redis
import typing
import uuid


def count_calls(method: typing.Callable) -> typing.Callable:
    """ Count calls Decorator """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """Wraps the crud function to add the count functionality"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: typing.Callable) -> typing.Callable:
    """ Count history Decorator """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """Wraps the crud function to add the historization functionality"""
        client: redis.Redis = self._redis
        client.rpush(method.__qualname__+':inputs', str(args))
        result = method(self, *args, **kwargs)
        client.rpush(method.__qualname__+':outputs', str(result))
        return result
    return wrapper


def replay(fn: typing.Callable) -> None:
    """ retrieve lists """
    client = redis.Redis()
    calls = client.get(fn.__qualname__).decode('utf-8')
    inputs = [input.decode('utf-8') for input in
              client.lrange(fn.__qualname__+":inputs", 0, -1)]
    outputs = [output.decode('utf-8') for output in
               client.lrange(fn.__qualname__+":outputs", 0, -1)]
    print("{} was called {} times:".format(fn.__qualname__, calls))
    for input, output in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(fn.__qualname__, input, output))


class Cache:
    """
    Caching class wraps redis
    """
    def __init__(self) -> None:
        """ The constructor of the cahing class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
