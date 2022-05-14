from flask import Flask

from docs import global_docs
from flask_api_doc.swagger import FlaskDocs
from flask_api_doc.blueprint import DocBlueprint

app = Flask(__name__)
app.config["DEBUG"] = True
swagger_docs = FlaskDocs(app)

docs = DocBlueprint("swagger", __name__, url_prefix="/docs")

@docs.get("/demo")
def docs_demo():
    """
    this is a demo
    :return:
    """
    return {"data": "demo"}


app.register_blueprint(docs)


if __name__ == '__main__':
    app.run()
    # print(global_docs.swagger_doc)