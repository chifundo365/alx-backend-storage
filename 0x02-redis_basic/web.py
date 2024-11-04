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

        key = "count:{}".format(url)
        r.incr(key)
        r.expire(key, 10)
        print("{}:{}".format(key, r.get(key)))
        output = func(url)
        return output
    return wrapper


@count_url_request_times
def get_page(url: str) -> str:
    """ Get content of a requested url """
    r = requests.get(url)
    return r.text
