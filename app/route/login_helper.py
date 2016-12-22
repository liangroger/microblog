#coding=utf-8

import json

from flask import request
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from util import const
from util import db_util
from app import config
from app import login_manager
from module.admin_user import admin_user_svc
from module.login_data import LoginData


### 登录登出公共函数
@login_manager.user_loader
def load_user(user_id):
    conn = db_util.getConnection(config)
    admin_info = admin_user_svc.getAdminUserInfo(conn, user_id)
    if admin_info == None:
        return None
    login_data = LoginData(user_id,
                           admin_info.get('login_name', ''),
                           admin_info.get('name'))
    return login_data


### 根据请求本身的参数来进行登录
# @login_manager.request_loader
# def load_user_from_request(request):
#     authorization_string = request.headers.get('X-Yigather-Authorization')
#     if not authorization_string:
#         return None
#
#     conn = db_util.getConnection(config)
#     admin_id = nonhuman_auth_svc.auth(conn, authorization_string)
#     if admin_id == None:
#         return None
#
#     admin_info = admin_user_svc.getAdminUserInfo(conn, admin_id)
#     if admin_info == None:
#         return None
#
#     login_data = LoginData(admin_id,
#                            admin_info.get('login_name', ''),
#                            admin_info.get('name'),
#                            admin_info.get('headimg_url'),
#                            admin_info.get('individual_id'))
#     return login_data


@login_manager.unauthorized_handler
def unauthorized():
    resp = {'errcode': const.ERRCODE_LOGIN_IS_REQUIED,
            'errmsg': const.strerr(const.ERRCODE_LOGIN_IS_REQUIED)}
    return json.dumps(resp, ensure_ascii=False)
