#!/usr/bin/env python3
"""
Implents a url client and a decorator func
"""
import requests
import redis
from functools import wraps
from typing import Callable, Tuple, Dict


def count_url_request_times(func: Callable) -> str:
    """ decorator func that count number of times a url was requested """
    @wraps(func)
    def wrapper(*args: Tuple, **kwargs: Dict) -> str:
        """ wrapper """
        r = redis.Redis()

        url = str(*args)

        r.incr("count:{}".format(url))
        result = r.get("result:{}".format(url))

        if result:
            return result.decode('utf-8')
        result = func(url)
        r.setex("result:{}".format(url), 10, result)
        return result
    return wrapper


@count_url_request_times
def get_page(url: str) -> str:
    """ Get content of a requested url """
    r = requests.get(url)
    return r.text
