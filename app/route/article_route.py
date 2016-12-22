#coding=utf-8
from flask import json
from flask import request

from app import app
from app import config
from module.article import article_srv
from util import const
from util import db_util
from util import util


@app.route("/list_article",methods=["Get","Post"])
def list_article():
    #可选和必选的参数
    allowed_param_list = ['category_id']
    required_param_list = []
    param_dict = {}
    for p in allowed_param_list:
        value = util.extract_arg_from_req(request, p)
        if value == '':
            if p in required_param_list:
                app.logger.warning('failed to get_education_history, lack of parameter: %s',
                                   p, extra=util.req_as_dict(request))
                return util.make_err_json_response(const.ERRCODE_LACK_OF_PARAMETER, {"param_name": p})
        else:
            param_dict[p] = value
    ## page－显示第几页， rows－每页显示多少行
    page, rows = util.extract_page_arg_from_req(request)

    conn = db_util.getConnection(config)
    try:
        total, entry_list = article_srv.list_article(conn, param_dict, page, rows)

        app.logger.info('list_article', extra=util.req_as_dict(request))
        resp = {'errcode': 0, 'total_rows': total, 'result': entry_list}
        return json.dumps(resp, default=util.defaultSerializer, ensure_ascii=False)

    except Exception, e:
        app.logger.warning('failed to list_article, exception:%s',
                           str(e), extra=util.req_as_dict(request))
        return util.make_err_json_response(const.ERRCODE_INTERNAL_ERR)

    finally:
        conn.close()

@app.route("/article",methods=["Get","Post"])
def article():
    entry_id = util.extract_arg_from_req(request, 'id')
    if entry_id == '':
        app.logger.warning('failed to get_article_entry, lack of parameter: id',
                           extra=util.req_as_dict(request))
        return util.make_err_json_response(const.ERRCODE_LACK_OF_PARAMETER, {"param_name": "id"})

    conn = db_util.getConnection(config)
    try:
        entry = article_srv.getArticleEntry(conn, entry_id)
        if entry == None:
            app.logger.warning('failed to get_article_entry, no such entry: %s',
                               entry_id, extra=util.req_as_dict(request))
            return util.make_err_json_response(const.ERRCODE_NO_SUCH_ENTRY)

        app.logger.info('get_article_entry', extra=util.req_as_dict(request))
        resp = {'errcode': const.ERRCODE_SUCC, 'result': entry}
        return json.dumps(resp, default=util.defaultSerializer, ensure_ascii=False)

    except Exception, e:
        app.logger.warning('failed to get_article_entry, exception:%s',
                           str(e), extra=util.req_as_dict(request))
        return util.make_err_json_response(const.ERRCODE_INTERNAL_ERR)

    finally:
        conn.close()