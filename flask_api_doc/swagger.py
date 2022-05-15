from flask import Flask

from docs import global_docs


class FlaskDocs:
    """
        需要在 flask 试图注册完毕之后的初始化
    """
    schemas = global_docs

    def __init__(self,
                 app: Flask = None):

        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.extensions['flask_api_doc'] = self

        # app is not debug mode
        if app.config.get("DEBUG") or True:
            # 在 flask config 中加载 swagger 配置
            global_docs.schemas["swagger"] = app.config.get("SWAGGER_VERSION", "2")
            global_docs.schemas["info"] = dict()
            global_docs.schemas["info"]["title"] = app.config.get("SWAGGER_TITLE", app.name)
            global_docs.schemas["info"]["description"] = app.config.get("SWAGGER_DESCRIPTION", app.name)
            global_docs.schemas["info"]["version"] = app.config.get("SWAGGER_VERSION", "2")
            global_docs.schemas["host"] = app.config.get("SWAGGER_HOST")
            global_docs.schemas["basePath"] = app.config.get("SWAGGER_BASE_URL")
            global_docs.schemas["schemas"] = app.config.get("SWAGGER_SCHEMAS", ["http"])
            global_docs.schemas["servers"] = app.config.get("SWAGGER_SERVERS", [
                {"description": "localhost swagger doc", "server": "http://localhost:5000"}])
            global_docs.schemas["components"] = app.config.get("SWAGGER_COMPONENTS")

            # register swagger json api
            from flask_api_doc.view import docs as ds
            app.register_blueprint(ds)

    @property
    def swagger_doc(self):
        return global_docs.swagger_doc
