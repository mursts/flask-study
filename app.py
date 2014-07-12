#!/usr/bin/env python
# coding: utf-8

from flask import Flask
import views

app = Flask(__name__)

def register_blueprints():
    app.register_blueprint(views.blueprint)

register_blueprints()

print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
