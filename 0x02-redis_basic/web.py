#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from functools import wraps


def keep_count_decorator(fn):
    """ Decorator to count page access """

    @wraps(fn)
    def wrapper(url: str) -> str:
        """ wrapper logic function """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'content:{url}')
        if cached_page:
            return cached_page.decode('utf-8')

        response = fn(url)
        client.set(f'content:{url}', response)
        client.expire(f'content:{url}', 10)
        return response
    return wrapper


@keep_count_decorator
def get_page(url: str) -> str:
    """keep track of reqs"""
    return requests.get(url).text
