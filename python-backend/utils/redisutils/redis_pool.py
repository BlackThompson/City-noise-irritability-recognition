import redis

from utils import config
from utils.wrapper import singleton

@singleton
class RedisPool():

    pool = None

    def __init__(self) -> None:
        self.pool = redis.ConnectionPool(host=config.REDIS_HOST, port=config.REDIS_PORT)

# 单例
# redis_pool = RedisPool()