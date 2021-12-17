#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy  # mysqlclient flask-sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@192.168.0.8:3307/dcshop'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_COMMIT_TEARDOWN"] = True
db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username

# db.Model    # 创建模型,
# db.Column   # 创建模型属性.

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""
        return '<Role %r>' % self.username


def get_user_data():
    result = User.query.all()
    user_list = [{'id': v.id, 'username': v.username} for v in result]
    return user_list


@app.route('/')
def home_index():
    return 'Hello World'


@app.route('/api/users/login')
def users_login():
    user_list = get_user_data()
    return jsonify(user_list), 200


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return 'Not found page', 404


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # get_user_data()
    app.run(host='0.0.0.0', debug=True, port=5000)
