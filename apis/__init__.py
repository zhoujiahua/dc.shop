#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Flask
from . import users

app = Flask(__name__)


def create_app():
    app.register_blueprint(users.user_api, url_prefix='/user')
    return app
