import json
from flask_cors import *
from flask import Blueprint, request, session, jsonify
from flask_login import LoginManager
# 创建蓝图
from tutorial.user.crud import User
from tutorial.user.schemas import LoginForm
from flask import render_template, redirect, url_for, request
from flask_login import login_user

from tutorial.user.user_data import get_user, USERS

user_bp = Blueprint('user', __name__)

login_manager = LoginManager()
login_manager.login_view = 'login'  ###跳转登录的地址
login_manager.session_protection = 'strong'

"""
@user_bp.route('/login', methods=('GET', 'POST'))  # 登录
def login():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_info = get_user(user_name)  # 从用户数据中查找用户记录
        if user_info is None:
            emsg = "用户名或密码密码有误"
        else:
            user = User(user_info)  # 创建用户实体
            if user.verify_password(password):  # 校验密码
                login_user(user)  # 创建用户 Session
                return redirect(request.args.get('next') or url_for('index'))
            else:
                emsg = "用户名或密码密码有误"
    return jsonify({"emsg": emsg, "form": str(form)})
"""


@user_bp.route('/login', methods=('GET', 'POST'))  # 登录
@cross_origin()
def login():
    form = LoginForm()
    user_name = form.username.data
    password = form.password.data
    if request.method == 'POST':
        try:
            user_info = get_user(user_name)
            user = User(user_info)
            password = user.verify_password(password)
            if password:
                return jsonify({"status": 200, "msg": "post_success"})

            else:
                return jsonify({"status": 401, "msg": "密码有误"})
        except AttributeError as e:
            return jsonify({"status": 400, "msg": "您没有这个账户", 'error': str(e)})

    else:
        return jsonify({"status": 204, "msg": "get_success"})
