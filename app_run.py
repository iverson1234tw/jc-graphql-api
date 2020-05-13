#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
#coding:utf-8

from flask import abort, jsonify, json, Response, request
from flask_graphql import GraphQLView
from schema import schema
from __init__ import *

app.add_url_rule('/graphql', view_func=GraphQLView.as_view("graphql",
    schema=schema, graphiql=True))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

if __name__ == "__main__":
    app.run(port=4901)