# -*- encoding: utf-8 -*-

"""
@File    :   consumer.py
@Time    :   2021/04/30 23:23:58
@Author  :   silist
@Version :   1.0
@Desc    :   负责从redis读消息
"""

import time
import redis
from utils.redisutils.redis_pool import RedisPool

class RedisConsumer():

    QUEUE = None

    client = None

    sleep_time = 5

    def __init__(self, queue) -> None:
        pool = RedisPool().pool
        self.client = redis.Redis(connection_pool=pool)
        self.QUEUE = queue

    def consume(self, func):
        while True:
            try:
                msg = self.client.brpop(self.QUEUE, timeout=2 * 60)
                if not msg:
                    continue
                for m in msg:
                    m = str(m, encoding='utf-8')
                    if m == self.QUEUE:
                        continue
                    func(m)
            except Exception as e:
                print("[ERROR] Consumer: %s" % e)
            finally:
                time.sleep(self.sleep_time)

