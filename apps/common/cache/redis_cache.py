# coding=utf-8
"""
    @project: maxkb
    @Author：虎
    @file： reis_cache.py
    @date：2024/3/6 11:20
    @desc:
"""
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache.backends.redis import RedisCache


class RedisMemCache(RedisCache):

    def clear_by_application_id(self, application_id):
        delete_keys = []
        for key in self._cache.get_client().scan_iter():
            value = self._cache.get(key)
            if (hasattr(value,
                        'application') and value.application is not None and value.application.id is not None and
                    str(
                        value.application.id) == application_id):
                delete_keys.append(key)
        for key in delete_keys:
            self.delete(key)

