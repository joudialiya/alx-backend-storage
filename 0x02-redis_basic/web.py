#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from functools import wraps
from typing import Callable


def keep_count_decorator(fn: Callable) -> Callable:
    """ Decorator to count page access """

    @wraps(fn)
    def wrapper(url: str) -> str:
        """ wrapper logic function """
        client = redis.Redis()
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')

        response = fn(url)
        client.set(f'{url}', response, 10)
        client.incr(f'count:{url}')
        return response
    return wrapper


@keep_count_decorator
def get_page(url: str) -> str:
    """keep track of reqs"""
    return requests.get(url).text
