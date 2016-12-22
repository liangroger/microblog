#coding=utf-8

import json

from flask import request
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from util import db_util
from util import util
from util import const
from app import config
from app import app
import login_helper

from module.admin_user import admin_user_svc


@app.route("/login", methods=["GET", "POST"])
def login():
    login_name = util.extract_arg_from_req(request, 'login_name')
    if login_name == '':
        app.logger.warning('failed to login, lack of parameter: login_name',
                           extra=util.req_as_dict(request))
        resp = {'errcode': const.ERRCODE_LACK_OF_PARAMETER,
                'errmsg': const.strerr(const.ERRCODE_LACK_OF_PARAMETER, {"param_name":"login_name"})}
        return json.dumps(resp, ensure_ascii=False)
    
    password = util.extract_arg_from_req(request, 'password')
    if password == '':
        app.logger.warning('failed to login, lack of parameter: password',
                           extra=util.req_as_dict(request))
        resp = {'errcode': const.ERRCODE_LACK_OF_PARAMETER,
                'errmsg': const.strerr(const.ERRCODE_LACK_OF_PARAMETER, {"param_name":"password"})}
        return json.dumps(resp, ensure_ascii=False)
    
    conn = db_util.getConnection(config)
    try:
        errcode, login_data = admin_user_svc.verifyLogin(conn, login_name, password)
        app.logger.debug('%s login', login_name, extra=util.req_as_dict(request))
            
        if errcode != const.ERRCODE_SUCC:
            app.logger.warning('failed to login, errcode=%d', errcode, extra=util.req_as_dict(request))
            resp = {'errcode': errcode,
                    'errmsg': const.strerr(errcode)}
            return json.dumps(resp, ensure_ascii=False)
        
        conn.commit()
        login_user(login_data)
        app.logger.info('login', extra=util.req_as_dict(request))
        resp = {'errcode': const.ERRCODE_SUCC}
        return json.dumps(resp, ensure_ascii=False)
    
    except Exception, e:
        app.logger.warning('failed to login, exception:%s, login_name:%s',
                           str(e), login_name, extra=util.req_as_dict(request))
        resp = {'errcode': const.ERRCODE_INTERNAL_ERR,
                'errmsg': const.strerr(const.ERRCODE_INTERNAL_ERR)}
        return json.dumps(resp, ensure_ascii=False)
    
    finally:
        conn.close()


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    resp = {'errcode': const.ERRCODE_SUCC}
    return json.dumps(resp, ensure_ascii=False)


@app.route("/check_login", methods=["GET", "POST"])
@login_required
def checkLogin():
    resp = {'errcode': const.ERRCODE_SUCC,
            'result': {
                'id': current_user.get_id(),
                'name': current_user.get_name(),
                'login_name': current_user.get_login_name()}
           }
    return json.dumps(resp, ensure_ascii=False)
