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


def call_history(method: Callable) -> Callable:
    """ Creates keys of called functions inputs and outputs """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper """
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        output = str(method(self, *args, **kwargs))

        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, output)

        return output
    return wrapper


def replay(fn: Callable) -> None:
    """ Display the history of calls of a particular function """
    r = redis.Redis()
    function_name = fn.__qualname__
    value = r.get(function_name)

    try:
        value = int(value.decode('utf-8'))
    except Exception:
        value = 0

    print('{} was called {} times:'.format(function_name, value))

    inputs = r.lrange('{}:inputs'.format(function_name), 0, -1)
    outputs = r.lrange('{}:outputs'.format(function_name), 0, -1)

    for input, output in zip(inputs, outputs):
        try:
            input = input.decode('utf-8')
        except Exception:
            input = ''

        try:
            output = output.decode('utf-8')
        except Exception:
            output = ''

        print('{}(*{}) -> {}'.format(function_name, input, output))


class Cache:
    def __init__(self) -> None:
        """ Initialise Redis Client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
