#coding=utf-8

DEFAULT_PAGE = 1
DEFAULT_ROWS = -1


DEFAULT_ROWS_PER_PAGE = 20

# 错误代码
ERRCODE_SUCC = 0

# 严重错误
ERRCODE_INTERNAL_ERR = 20000 

# 参数不正确
ERRCODE_LACK_OF_PARAMETER = 21001
ERRCODE_INVALID_PHONE_NUMBER = 21002
ERRCODE_INVALID_DATETIME = 21003
ERRCODE_INVALID_STATUS = 21004
ERRCODE_INVALID_EVENT_TYPE = 21005
ERRCODE_NAME_ALREADY_EXISTS = 21006
ERRCODE_PHONE_NUMBER_ALREADY_EXISTS = 21007


# 登录和权限
ERRCODE_LOGIN_IS_REQUIED = 22001
ERRCODE_NO_SUCH_USER_OR_WRONG_PASSWORD = 22002
ERRCODE_NOT_ALLOWED_TO_DO = 22003

# 没有这个人
ERRCODE_NO_SUCH_INDIVIDUAL_FILE = 23001
ERRCODE_NO_SUCH_PHONE_NUMBER = 23002
ERRCODE_NO_SUCH_EMAIL = 23003
ERRCODE_NO_SUCH_PEOPLE = 23004

# 没有这个社交账号
ERRCODE_NO_SUCH_SOCIAL_MEDIA_ACCOUNT = 24001

# 没有这条记录
ERRCODE_NO_SUCH_ENTRY = 25001

# 没有这个活动
ERRCODE_NO_SUCH_ACTIVITY = 25001


# 错误消息，中文UTF-8
err_msg_dict = {
    ERRCODE_SUCC: '',
    
    ERRCODE_INTERNAL_ERR: "系统错误",
    
    ERRCODE_LACK_OF_PARAMETER: "缺少参数",
    ERRCODE_INVALID_PHONE_NUMBER: "手机号码不正确",
    ERRCODE_INVALID_DATETIME: "日期/时间不正确",
    ERRCODE_INVALID_STATUS: "状态值不正确",
    ERRCODE_INVALID_EVENT_TYPE: "事件代码不正确",
    
    ERRCODE_NAME_ALREADY_EXISTS: "该名称已经存在了",
    ERRCODE_PHONE_NUMBER_ALREADY_EXISTS: "该手机号已存在了",
    
    ERRCODE_LOGIN_IS_REQUIED: "请重新登录",   
    ERRCODE_NO_SUCH_USER_OR_WRONG_PASSWORD: "登录失败, 没有这个用户或者密码错误",
    ERRCODE_NOT_ALLOWED_TO_DO: "没有足够的权限执行此操作",
    
    ERRCODE_NO_SUCH_INDIVIDUAL_FILE: "该用户帐号不存在",
    ERRCODE_NO_SUCH_PHONE_NUMBER: "该手机号码不存在",
    ERRCODE_NO_SUCH_EMAIL: "该email不存在",
    ERRCODE_NO_SUCH_PEOPLE: "此账号不存在",
    
    ERRCODE_NO_SUCH_SOCIAL_MEDIA_ACCOUNT: "该社交媒体账号不存在",
    
    ERRCODE_NO_SUCH_ENTRY: "这条记录不存在",
    
    ERRCODE_NO_SUCH_ACTIVITY: "这个活动/事件／项目不存在"
}

def strerr(errcode, param_dict = None):
    if errcode == ERRCODE_LACK_OF_PARAMETER:
        param_name = ''
        if param_dict is not None:
            param_name = param_dict.get('param_name', '')
        return err_msg_dict[errcode] + param_name
    return err_msg_dict.get(errcode, "未知错误")




