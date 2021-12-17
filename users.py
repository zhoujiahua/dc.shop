#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Blueprint

user_api = Blueprint('user_api', __name__)


@user_api.route('/login')
def user_login():
    return 'User login information.'


@user_api.route('/register')
def user_login():
    return 'User register information.'
