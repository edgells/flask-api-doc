from enum import Enum
from typing import Sequence, Dict, Type, cast, List

from pydantic import BaseModel
from pydantic.fields import ModelField

from params import ParamsType


field_map = {
    str: "string",
    list: "array",
    bool: "boolean",
    int: "integer",
}


def get_openapi_operation_parameters(request_model: Type[BaseModel]):
    """
    get in
    get name
    get required
    get schema
    :param request_model:
    :return:
    """
    parameters = []
    for field in request_model.__fields__:
        field = request_model.__fields__[field]
        parameters.append({
            "name": field.alias,
            "required": field.field_info.extra.get("required", False),
            "in": field.field_info.extra.get("in_", ParamsType.query).value,
            "description": field.field_info.extra.get("description", ""),
            "schema": {
                "title": field.alias,
                "type": field_map[field.outer_type_]
            }
        })

    return parameters

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
            schema_doc["properties"][item]["title"] = item

        if schema["properties"][item].get("type"):
            schema_doc["properties"][item]["type"] = schema["properties"][item]["type"]

        schema_doc["properties"][item]["description"] = schema["properties"][item].get("description")

    return schema_doc

def marshal_response(data):
    if isinstance(data, BaseModel):
        return data.json()

