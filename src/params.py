from enum import Enum

from flask import request
from pydantic import BaseModel as bm


class ParamsType(Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"


class BaseModel(bm):

    @classmethod
    def parser_args(cls, strict=False, req=None):

        if not req:
            req = request

        # param validator
        params = {}
        field_meta = cls.__fields__
        for field in field_meta:
            # 处理参数位置
            field_flag = field_meta[field].field_info.extra
            if field_flag.get("in_"):
                field_flag = field_flag.get("in_")

            else:
                field_flag = ParamsType.query

            # 根据位置获取参数
            if field_flag == ParamsType.query:
                params.update(req)
