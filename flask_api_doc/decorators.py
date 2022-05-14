import functools
from typing import Type

from pydantic import BaseModel


def api(summary,
        description,
        version,
        request_model: Type[BaseModel],
        response_model: Type[BaseModel],
        tags=None,
        **kwargs):
    """
    视图文档装饰器， 定义一个 swagger path 对象
    :param summary:
    :param description:
    :param version:
    :param kwargs:
    :return:
    """
    def decorator(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            # 注册文档

            return func(*args, **kwargs)

        return wrap

    return decorator


def auth_decorator(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):


        return func(*args, **kwargs)
    return wrap