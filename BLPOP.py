#! /usr/bin/env python
# coding=utf-8
# author: Rand01ph

import time
import json
from _redis2 import RedisQueue

rq = RedisQueue("nsfocus:test")

while True:
    result = rq.get(True)
    print result
    time.sleep(1)
