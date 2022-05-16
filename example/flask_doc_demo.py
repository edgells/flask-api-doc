from typing import Optional

from flask import Flask
from pydantic import BaseModel, Field

from flask_api_doc.blueprint import DocBlueprint
from flask_api_doc.swagger import FlaskDocs
from params import ParamsType

app = Flask(__name__)
app.config["DEBUG"] = True
swagger_docs = FlaskDocs(app)

docs = DocBlueprint("swagger_demo", __name__, url_prefix="/docs")


class UserModel(BaseModel):
    username: Optional[str] = Field("lie", description="用户名称", required=True, in_=ParamsType.path)
    password: Optional[str] = Field("lie123", description="用户密码", required=True, in_=ParamsType.query)


@docs.get("/demo/<string:username>", request_model=UserModel, response_model=UserModel)
def docs_demo(username):
    """
    this is a demo
    :return:
    """
    return {"data": username}


app.register_blueprint(docs)

if __name__ == '__main__':
    app.run()
    # print(global_docs.swagger_doc)
    # for blue in app.iter_blueprints():
    #     print(blue)
    # for field in UserModel.__fields__:
    #     print(UserModel.__fields__[field].field_info.extra)
    # print(UserModel().schema())