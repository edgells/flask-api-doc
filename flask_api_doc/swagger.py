import socket
from typing import Type

from flask import Flask, jsonify, render_template
from pydantic import BaseModel


class FlaskDocs:
    """
        需要在 flask 试图注册完毕之后的初始化
    """

    def __init__(self,
                 app: Flask=None,
                 base_url="",
                 doc="/docs",
                 version="1.0",
                 doc_version="1.0",
                 host=socket.gethostname(),
                 title=None,
                 description=None,
                 terms_url=None,
                 license=None,
                 license_url=None,
                 contact=None,
                 contact_url=None,
                 contact_email=None,
                 authorizations=None,
                 security=None,
                 servers=None,
                 components=None):

        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.extensions['flask_api_doc'] = self

        # app is not debug mode
        if app.config.get("DEBUG") or True:
            # register swagger json api
            from flask_api_doc.view import docs as ds
            app.register_blueprint(ds, "/swagger")



