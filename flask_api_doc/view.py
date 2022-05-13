"""
flask swagger api doc view
"""
from flask import Blueprint, render_template


docs = Blueprint("docs", __name__)

@docs.get("/swagger_ui_html")
def swagger_template():
    return render_template("swagger_template.html")

@docs.get("/swagger.json")
def swagger_json():
    return