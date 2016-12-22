#coding=utf-8
from flask import json
from flask import request

from app import app
from app import config
from util import const
from util import util
from util import db_util
from module.category import category_srv

@app.route("/list_category",methods=["Get","Post"])
def list_category():
    parent_id = util.extract_arg_from_req(request,"parent_id")
    if parent_id == '':
        parent_id = '0'

    conn = db_util.getConnection(config)
    try:
        list_data = category_srv.getCategoryList(conn,parent_id)

        conn.commit()
        app.logger.info('login', extra=util.req_as_dict(request))
        resp = {'errcode': const.ERRCODE_SUCC,
                'result': list_data}
        return json.dumps(resp, ensure_ascii=False)
    except Exception, e:
        app.logger.warning('failed to list_category, exception:%s, parent_id:%s',
                           str(e), parent_id, extra=util.req_as_dict(request))
        resp = {'errcode': const.ERRCODE_INTERNAL_ERR,
                'errmsg': const.strerr(const.ERRCODE_INTERNAL_ERR)}
        return json.dumps(resp, ensure_ascii=False)
    finally:
        conn.close()