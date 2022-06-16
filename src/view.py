"""
flask swagger api doc view
"""
from flask import Blueprint, render_template, jsonify, url_for

from docs import global_docs

docs = Blueprint("docs", __name__, url_prefix="/swagger", template_folder="./templates", static_folder="./static")

@docs.add_app_template_global
def swagger_static(filename):
    return url_for("docs.static", filename=filename)

@docs.get("/swagger_ui.html")
def swagger_template():
    return render_template("swagger-ui.html", title=global_docs.schemas["info"]["title"], specs_url="/swagger/swagger.json")

@docs.get("/swagger.json")
def swagger_json():
    return jsonify(global_docs.schemas)