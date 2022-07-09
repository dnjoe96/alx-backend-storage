#!/usr/bin/env python3
"""Module defines `Cache` class"""
import redis
from typing import Union, Optional, Callable, Any
from uuid import uuid4
import functools


def count_calls(method: Callable) -> Callable:
    """ record the number of time method is called
    Args:
        method (Callable): The decorated function
    Returns:
        Wrapper function
    """
    @functools.wraps(method)
    def count_calls_wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """ Wrapper method for provided wrapped method """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return count_calls_wrapper


class Cache:
    """Cache class"""
    DB_VAL_TYPS = Union[str, bytes, int, float, None]

    def __init__(self) -> None:
        """Constructor method for class `Cache` class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[bytes, float, int, str]) -> str:
        """A function that store data in a unique key
        Args:
            data (str, bytes, int, float): data to save as value
        Returns:
            Unique key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> DB_VAL_TYPS:
        """ Method to get value at `key`
        Args:
            key (str): The key
            fn (Callable): Function that decodes to utf-8
        Returns:
            data from server
        """
        raw_data = self._redis.get(key)
        if fn is not None:
            return fn(raw_data)
        else:
            return raw_data

    def get_str(self, data: bytes) -> str:
        """ Method returns string type-casted data """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Method returns integer type-casted data """
        return int(data)
