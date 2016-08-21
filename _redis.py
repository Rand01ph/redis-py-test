#! /usr/bin/env python
# coding=utf-8
# author: Rand01ph

import redis

class RedisClient(redis.StrictRedis):

    _instance = None

    def __init__(self, server):
        redis.StrictRedis.__init__(self, **server)


    def __new__(cls, *args):
        if not cls._instance:
            cls._instance = super(RedisClient, cls).__new__(cls)
        return cls._instance

REDIS_SERVER = {
'host': '127.0.0.1',
'port': 6379
}

rc = RedisClient(REDIS_SERVER)
