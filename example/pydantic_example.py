from typing import List

from pydantic import BaseModel, validator, Field
from fastapi import Path


class UserModel(BaseModel):
    username: str = Field(None, title="用户名称", description="用户名称", min_length=5, max_length=100, exclude=True)
    password: str


# pydantic 验证
class UserValidator(BaseModel):
    username: str
    password: str
    tagList: List[int] = []

    @validator("*", pre=True)
    def trim_name(cls, v):
        if isinstance(v, str):
            return v.strip(" ")

    @validator("username")
    def check_username(cls, v):
        return v

    @validator("tagList", each_item=True)  # each_item 会针对可迭代对象每个元素进行处理
    def check_password(cls, v):
        assert v > 1
        return v * 2


if __name__ == '__main__':
    print(UserModel(password="helll").dict())