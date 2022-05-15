from pydantic import BaseModel, validator, ValidationError
from pydantic import Field
from typing_extensions import Annotated

from params import ParamsType


class UserProfile(BaseModel):
    username: str = Field(None, title="", min_length=5, max_length=10)



if __name__ == '__main__':
    try:
        userProfile = UserProfile(username="hell")

    except ValidationError as e:
        for r_error in e.raw_errors:
            print(r_error.exc)