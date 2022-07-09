#!/usr/bin/env python3
"""Module defines `Cache` class"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """Cache class"""
    DB_VAL_TYPS = Union[str, bytes, int, float, None]

    def __init__(self) -> None:
        """Constructor method for class `Cache` class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
