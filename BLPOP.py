#! /usr/bin/env python
# coding=utf-8
# author: Rand01ph

import time
from _redis import rc

while True:
    result = rc.blpop("nsfocus:test", 0)
    print result
    time.sleep(1)
