# -*- encoding: utf-8 -*-

"""
@File    :   producer.py
@Time    :   2021/05/01 16:19:07
@Author  :   silist
@Version :   1.0
@Desc    :   向redis发送消息
"""

import redis
from utils.redisutils.redis_pool import RedisPool

class RedisProducer():

    QUEUE = None

    client = None

    def __init__(self, queue) -> None:
        pool = RedisPool().pool
        self.client = redis.Redis(connection_pool=pool)
        self.QUEUE = queue

    def produce(self, msg):
        try:
            print("[INFO] Producer: Send: %s" % msg)
            res = self.client.lpush(self.QUEUE, msg)
            # print(res)
        except Exception as e:
            print("[ERROR] Producer: %s" % e)
