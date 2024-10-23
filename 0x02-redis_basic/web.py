#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from functools import wraps
from typing import Callable


def keep_count_decorator(fn: Callable) -> Callable:
    """ Decorator to count page access """
    client = redis.Redis()

    @wraps(fn)
    def wrapper(url: str) -> str:
        """ Wrapper function """
        key = "count:{}".format(url)
        client.incr(key)

        cached_page = client.get("result:{}".format(url))
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set("result:{}".format(url), response, 10)
        return response
    return wrapper


@keep_count_decorator
def get_page(url: str) -> str:
    """keep track of reqs"""
    return requests.get(url).text
