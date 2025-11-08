import os
from dotenv import load_dotenv
import redis.asyncio as redis


load_dotenv()


class Redis():
    def __init__(self):
        """initialize  connection """
        self.REDIS_URL = os.environ.get('REDIS_URL', 'redis://redis:6379')
        self.REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')
        self.REDIS_USER = os.environ.get('REDIS_USER', 'default')
        self.REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
        self.REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))

    async def create_connection(self):
        self.connection = redis.from_url(
            self.REDIS_URL, db=0)

        return self.connection

    async def create_rejson_connection(self):
        self.redisJson = redis.from_url(
            self.REDIS_URL, db=0, decode_responses=True)

        return self.redisJson
