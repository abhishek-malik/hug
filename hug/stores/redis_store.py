import redis
from hug.logger_mixin import LoggerMixin

class RedisStore:
    def __init__(self, host='localhost', port=6379, db=0, ttl=3600, logger_name="hug"):
        super().__init__(logger_name)

        self._client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)
        self._ttl = ttl

    def get(self, key):
        try:
            return self._client.hgetall(key)
        except redis.RedisError as e:
            self._logger.exception(f"Redis Error: {e}")
            return {}
        except Exception as e:
            self._logger.exception(f"Redis Exception: {e}")
            return {}

    def set(self, key, data):
        try:
            self._client.hmset(key, data)
            self._client.expire(key, self._ttl)
        except redis.RedisError as e:
            self._logger.exception(f"Redis Error: {e}")
            raise
        except Exception as e:
            self._logger.exception(f"Redis Exception: {e}")
            raise

    def exists(self, key):
        try:
            return self._client.exists(key)
        except redis.RedisError as e:
            self._logger.exception(f"Redis Error: {e}")
            raise
        except Exception as e:
            self._logger.exception(f"Redis Exception: {e}")
            raise

    def delete(self, key):
        try:
            self._client.delete(key)
        except redis.RedisError as e:
            self._logger.exception(f"Redis Error: {e}")
            raise
        except Exception as e:
            self._logger.exception(f"Redis Exception: {e}")
            raise
        