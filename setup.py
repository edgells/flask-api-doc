from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask-Docs",
    version="1.0",
    url="https://github.com/edgells/flask-docs",
    license="MIT",
    author="edgells",
    description="用于 flask api 文档构建",
    py_modules=["flask_api_docs"],
    zip_safe=False,
    include_package_data=True,
    platform="any",
    install_requires=[
        "Flask >= 0.11.10",
        "pydantic >= 0.11.10",
        "importlib-metadata >= 3.6.0; python_version < '3.10'",
    ],
    extras_require={
        "async": ["asgiref >= 3.2"],
        "dotenv": ["python-dotenv"],
    },
)