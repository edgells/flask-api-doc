import typing as t
import os

from flask import Blueprint

from flask_api_doc.swagger import FlaskDocs

class DocBlueprint(Blueprint):
    """
    summary: 定义视图标签
    tags：添加视图组
    title：视图标题
    description：描述

    """
    _sentinel = object()

    def __init__(
            self,
            name: str,
            import_name: str,
            static_folder: t.Optional[t.Union[str, os.PathLike]] = None,
            static_url_path: t.Optional[str] = None,
            template_folder: t.Optional[str] = None,
            url_prefix: t.Optional[str] = None,
            subdomain: t.Optional[str] = None,
            url_defaults: t.Optional[dict] = None,
            root_path: t.Optional[str] = None,
            cli_group: t.Optional[str] = _sentinel,  # type: ignore
    ):
        super(DocBlueprint, self).__init__(
            name,
            import_name,
            static_folder,
            static_url_path,template_folder,
            url_prefix,
            subdomain, url_defaults, root_path, cli_group
        )
        FlaskDocs.add_tag(self.name)

    def add_url_rule(
            self,
            rule: str,
            endpoint: t.Optional[str] = None,
            view_func: t.Optional[t.Callable] = None,
            provide_automatic_options: t.Optional[bool] = None,
            **options: t.Any,
    ) -> None:
        # build doc
        method = options.pop("methods")[0] or "get"
        title = options.pop("title", view_func.__name__)

        view_schema = {
            method: {
                "summary": options.pop("summary", ""),
                "description": options.pop("description", view_func.__doc__),
                "deprecated": options.pop("deprecated", False),
                "title": title,
                "tags": [self.name],
                "parameters": [],
                "responses": {
                    "200": {
                        "schema": {

                        }
                    }
                }
            }
        }

        if options.get("response_model"):
            response_model = options.pop("response_model")
            view_schema[method]["responses"]["200"]["schema"]["description"] = response_model.__doc__

            refs = FlaskDocs.register_model(response_model)
            view_schema[method]["responses"]["200"]["schema"]["$ref"] = refs

        if options.get('tags'):
            FlaskDocs.add_tag(options.pop('tags'))

        FlaskDocs.add_path(rule, view_schema)

        # handle view register logic
        super(DocBlueprint, self).add_url_rule(
            rule,
            endpoint,
            view_func,
            provide_automatic_options,
            **options
        )
