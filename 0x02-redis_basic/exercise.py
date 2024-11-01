#!/usr/bin/env python3
""" Creates redis connection """
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count how many times a method was called """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self) -> None:
        """ Initialise Redis Client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a key and sets the data as the value in redis server """
        key = str(uuid4())
        self._redis[key] = data
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, int]:
        """
        Gets a value of a key in the format specified by the converter fn
        """
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, _bytes: bytes) -> str:
        """ converts bytes to string """
        return _bytes.decode('utf-8')

    def get_int(self, _bytes: bytes) -> int:
        """ Converts bytes to int """
        return int(_bytes.decode('utf-8'))
