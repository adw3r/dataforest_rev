import abc
import logging
from typing import NoReturn

import requests

from module import config


class ProxyPoolInterface:
    pool: list = []

    def __repr__(self):
        return self.proxy_pool_name

    def __init__(self, proxy_pool_name: str, **kwargs):
        self.proxy_pool_name = proxy_pool_name
        self.pool = self.get_pool()

    def __len__(self) -> int:
        return len(self.pool)

    @classmethod
    def get_pool_instance(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @abc.abstractmethod
    def pop(self) -> str:
        ...

    @abc.abstractmethod
    def get_pool(self) -> NoReturn:
        ...


class ProxyPool(ProxyPoolInterface):

    def pop(self) -> str:
        if len(self) == 0:
            self.get_pool()
        value = self.pool.pop()
        return value

    def get_pool(self) -> NoReturn:
        response = None
        url = f'http://{config.PROXIES_API_HOST}/proxies/{self.proxy_pool_name}?method=pool'
        while type(response) is not requests.Response:
            try:
                response = requests.get(url, timeout=10)
                content = response.content.decode().split('\n')
                self.pool = content
                return content
            except Exception as error:
                logging.error(error)
