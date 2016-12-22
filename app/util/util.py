#coding=utf-8
import json
import hashlib
import uuid
import time
import re
from xml.etree import ElementTree

import const

empty_extra = {'remote_addr': '', 'url':'', 'data':None}

def req_as_dict(req = None):
    if req == None:
        return {'remote_addr': '', 'url':'', 'data':None}
    
    d = {f: getattr(req, f, '') for f in ['remote_addr', 'url']}
    d['remote_addr'] = req.headers.get('X-Real-Ip', req.remote_addr)
    data = ''
    for k,v in req.form.items():
        data = data + ('%s=%s&' % (k,v))
    d['data'] = data
    return d

def extract_arg_from_req(req, k, default=''):
    return (k in req.form) and req.form[k] or (req.args.get(k, default))

def extract_page_arg_from_req(req):
    page_str = extract_arg_from_req(req, 'page')
    if page_str == '':
        page = const.DEFAULT_PAGE
    else:
        page = int(page_str)
    if page < 1:
        page = 1

    rows_str = extract_arg_from_req(req, 'rows')
    if rows_str == '':
        rows = const.DEFAULT_ROWS
    else:
        rows = int(rows_str)
    if rows < -1:
        rows = -1

    return page, rows

def make_err_json_response(errcode, extra_param_dict=None):
    resp = {'errcode': errcode,
            'errmsg': const.strerr(errcode, extra_param_dict)}
    return json.dumps(resp, ensure_ascii=False)


def defaultSerializer(obj):
    """Default JSON serializer."""
    import calendar, datetime, decimal

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        else:
            ## +08:00时区校正
            obj = obj - datetime.timedelta(hours=8)
        seconds = calendar.timegm(obj.timetuple())
        return seconds
    
    if isinstance(obj, decimal.Decimal):
        return float(obj)

## 检查是否合法的手机号
def is_valid_phone_number(phone_number):
    if not isinstance(phone_number, basestring):
        return False

    for c in phone_number:
        if not (c >= '0' and c <= '9'):
            return False
    return True

## 检查是否合法的身份证号
def is_valid_id_card_number(id_card_number):
    if not isinstance(id_card_number, basestring):
        return False

    # 长度一定是18个字符
    if len(id_card_number) != 18:
        return False
    
    # 第1～17位必须是数字
    for c in id_card_number[0:17]:
        if not (c >= '0' and c <= '9'):
            return False
    
    # 最后一位是数字或者小写英文字母
    c = id_card_number[-1]
    if (c >= '0' and c <= '9') or (c >= 'a' and c <='z'):
        return True 
    return False

## 检查是否合法的email地址
def is_valid_email(email):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return True
    return False

def isFloat(number_str):
    s = number_str.replace('.', '', 1)
    return s.isdigit()

def is_valid_datetime(datetime_str):
    try:
        time.strptime(datetime_str,"%Y-%m-%d %H:%M:%S")
    except:
        return False
    return True

def is_valid_date(date_str):
    try:
        time.strptime(date_str,"%Y-%m-%d")
    except:
        return False
    return True

def getMD5(src_str):
    m1 = hashlib.md5()
    m1.update(src_str)
    return m1.hexdigest().lower()

def getUUID():
    return str(uuid.uuid1())

def getBriefName(name, min_length=8):
    if min_length < 4:
        min_length = 4
    
    decoded_str = name.decode('utf-8')
    if len(decoded_str) < min_length:
        return name
    return decoded_str[0:(min_length-3)] + '...'

# 将XML转化为dict
def convertXMLtoDict(xml_string):
    root = ElementTree.fromstring(xml_string)
    d = {}
    for c in root:
        d[c.tag] = c.text
    return d


def getWeixinXMLResponse(return_code, return_msg):
    resp = '<xml>' \
            '<return_code>%s</return_code>' \
            '<return_msg>%s</return_msg>' \
           '</xml>' % (return_code, return_msg)
    return resp
