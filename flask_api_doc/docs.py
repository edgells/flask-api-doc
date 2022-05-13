import socket
from typing import Type

from pydantic import BaseModel


class SwaggerDoc:

    def __init__(self,
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
                 components=None
                 ):
        self.__schema = dict()
        self.version = version
        self.doc_version = doc_version
        self.base_url = base_url
        self.title = title
        self.description = description
        self.terms_url = terms_url
        self.license = license
        self.license_url = license_url
        self.contact = contact
        self.contact_url = contact_url
        self.contact_email = contact_email
        self.authorizations = authorizations
        self.security = security
        self.host = host
        self.docs = doc
        self.components = components
        self.servers = servers

    def init_schema(self):
        # 处理 swagger 文档，基础信息
        self.__schema["version"] = self.version
        self.__schema["basePath"] = self.base_url
        self.__schema["info"]["title"] = self.title
        self.__schema["info"]["description"] = self.description
        self.__schema["info"]["version"] = self.doc_version
        self.__schema["servers"] = self.servers

    @property
    def swagger_doc(self):
        # 处理 tags 重复
        tags = self.__schema["tags"]
        tags_tmp = {}
        for tag in tags:
            tags_tmp[tag['name']] = tag

        self.__schema['tags'] = tags_tmp.values()



        return self.__schema

    def register_model(self, response_model: Type[BaseModel]):
        # handle model
        schema = response_model.schema()

        definition = schema.pop(self.components)
        if definition:
            self.__schema[self.components].update(definition)

        self.__schema[self.components] = {
            response_model.__name__: schema
        }

        return "/".join(["#", self.components, response_model.__name__])

    def get_model(self, response_model: Type[BaseModel]):
        return self.__schema[self.components][response_model.__name__]

    def add_tag(self, tags):
        if not self.__schema.get("tags"):
            self.__schema["tags"] = []

        self.__schema["tags"].append({"name": tags})

    def add_path(self, path, view_schema):
        self.__schema["paths"][path] = view_schema


global_docs = SwaggerDoc()