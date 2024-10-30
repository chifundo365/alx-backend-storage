#!/usr/bin/env python3
""" Createsa redis connection """
import redis
from uuid import uuid4
from typing import Union, Callable


class Cache:
    def __init__(self) -> None:
        """ Initialise Redis Client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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

    def get_int(self, _bytes: bytes) => int:
        """ Converts bytes to int """
        return int(_bytes.decode('utf-8'))
