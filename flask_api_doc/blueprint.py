import os
import typing as t

from flask import Blueprint

from docs import global_docs
from utils import get_openapi_operation_parameters


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
            static_url_path, template_folder,
            url_prefix,
            subdomain, url_defaults, root_path, cli_group
        )
        # 添加视图分组标签
        global_docs.add_tag(self.name)

    def add_url_rule(
            self,
            rule: str,
            endpoint: t.Optional[str] = None,
            view_func: t.Optional[t.Callable] = None,
            provide_automatic_options: t.Optional[bool] = None,
            **options: t.Any,
    ) -> None:
        """
        解决当前视图函数是在哪个 blueprints 下的
        解决视图函数文档添加问题
        :param rule:
        :param endpoint:
        :param view_func:
        :param provide_automatic_options:
        :param options:
        :return:
        """
        #### build doc
        method = options.pop("methods")[0].lower() or "get"
        title = options.pop("title", view_func.__name__)
        api_description = options.pop("description", view_func.__doc__)
        view_schema = {
            method: {
                "summary": options.pop("summary", ""),
                "description": api_description,
                "deprecated": options.pop("deprecated", False),
                "operationId": title,
                "tags": [self.name],
                "parameters": [],
                "responses": {
                    "200": {
                        "schema": {},
                        "description": "success response"
                    }
                }
            }
        }

        # 处理请求参数文档
        if options.get("request_model"):
            request_model = options.pop("request_model")
            view_schema[method]["parameters"] = get_openapi_operation_parameters(request_model)

        # 处理视图响应文档
        if options.get("response_model"):
            response_model = options.pop("response_model")
            refs = global_docs.register_model(response_model)
            # 注册指定 model
            view_schema[method]["responses"]["200"]["schema"][
                "description"] = response_model.__doc__ or "Successful Response"
            view_schema[method]["responses"]["200"]["schema"]["$ref"] = refs

        if options.get('tags'):
            global_docs.add_tag(options.pop('tags'))

        global_docs.add_path(rule, view_schema)

        # handle view register logic
        super(DocBlueprint, self).add_url_rule(
            rule,
            endpoint,
            view_func,
            provide_automatic_options,
            **options
        )
