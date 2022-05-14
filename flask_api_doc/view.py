"""
flask swagger api doc view
"""
from flask import Blueprint, render_template, jsonify

from docs import global_docs

docs = Blueprint("docs", __name__, url_prefix="/swagger")

@docs.get("/swagger_ui_html")
def swagger_template():
    return render_template("swagger_template.html")

@docs.get("/swagger.json")
def swagger_json():
    return jsonify(global_docs.schemas), 200