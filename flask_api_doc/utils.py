from enum import Enum
from typing import Sequence, Dict, Type, cast

from pydantic import BaseModel
from pydantic.fields import ModelField


def get_openapi_operation_parameters():
    pass


def get_openapi_response_model(schema):
    schema_doc = {
        "title": schema.get("title"),
        "type": schema.get("type"),
        "properties": {

        }
    }

    for item in schema["properties"]:
        schema_doc["properties"][item] = {}
        if schema["properties"][item].get("title"):
            schema_doc["properties"][item]["title"] = schema["properties"][item]["title"]

        if schema["properties"][item].get("type"):
            schema_doc["properties"][item]["type"] = schema["properties"][item]["type"]

        if schema["properties"][item].get("description"):
            schema_doc["properties"][item]["description"] = schema["properties"][item]["description"]

    return schema_doc

def marshal_response(data):
    if isinstance(data, BaseModel):
        return data.json()

