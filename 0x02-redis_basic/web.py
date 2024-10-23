#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from typing import Callable


def keep_count_decorator(fn: Callable) -> Callable:
    client = redis.Redis()

    def wrapper(url: str) -> str:
        key = "count:{}".format(url)
        client.incr(key)

        cached_page = client.get(url)
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(url, response, 10)
        return response
    return wrapper


@keep_count_decorator
def get_page(url: str) -> str:
    """keep track of reqs"""
    return requests.get(url).text
