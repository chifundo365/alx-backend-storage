#!/usr/bin/env python3
""" Createsa redis connection """
import redis
from uuid import uuid4
from typing import Any


class Cache:
    def __init__(self) -> None:
        """ Initialise Redis Client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """ Generates a key and sets the data as the value in redis server """
        key = str(uuid4())
        self._redis[key] = data
        return key
