#coding=utf-8
import uuid

from util import const
from util import util
from login_data import LoginData

class AdminUserService:
    
    def getAdminUserList(self, db_conn, param_dict, page, rows):
        page = int(page)
        rows = int(rows)
        
        where_list = ['is_deleted=0']
        where_var_list = []

        if param_dict.get('keyword') != None:
            where_list.append('name like "%%' + param_dict.get('keyword') + '%%"')

        cursor = db_conn.cursor()
        sql_str_list = ['SELECT COUNT(*) as count FROM sys_user']
        sql_var_list = []
        if len(where_list) > 0:
            sql_str_list.extend(['WHERE', ' AND '.join(where_list)])
            sql_var_list.extend(where_var_list)

        cursor.execute(' '.join(sql_str_list), sql_var_list)
        total = 0
        t = cursor.fetchone()
        if t is not None:
            total = int(t["count"])

        sql_str_list = ['SELECT id, login_name, name FROM sys_user']
        sql_var_list = []
        if len(where_list) > 0:
            sql_str_list.extend(['WHERE', ' AND '.join(where_list)])
            sql_var_list.extend(where_var_list)

        if rows >= 0:
            offset = 0
            if page >= 1:
                offset = (page - 1) * rows
            sql_str_list.append('LIMIT %s, %s')
            sql_var_list.extend([offset, rows])
        cursor.execute(' '.join(sql_str_list), sql_var_list)
        result = cursor.fetchall()
        cursor.close()
        
        return total, result


    def getAdminUserInfo(self, db_conn, admin_id):
        cursor = db_conn.cursor()
        sql_str_list = ['SELECT id, login_name, name FROM sys_user WHERE id=%s']
        cursor.execute(' '.join(sql_str_list), [admin_id])
        result = cursor.fetchone()
        cursor.close()
        return result

    def verifyLogin(self, db_conn, login_name, password):
        cursor = db_conn.cursor()
        password_md5 = util.getMD5(password)
        cursor.execute("SELECT id, name FROM sys_user WHERE login_name=%s AND password=%s",
                       [login_name, password_md5])
        t = cursor.fetchone()
        cursor.close()
        if t == None:
            return const.ERRCODE_NO_SUCH_USER_OR_WRONG_PASSWORD, None
        
        data = LoginData(t["id"], login_name, t["name"])
        return const.ERRCODE_SUCC, data
    
    def createAdminUser(self, db_conn, param_dict):
        #new_id = 'A' + str(uuid.uuid1()).replace('-', '')
        password_md5 = util.getMD5(param_dict['password'])
        cursor = db_conn.cursor()
        cursor.execute('INSERT sys_user(login_name, name, password, last_login_time) '
                       ' VALUES(%s, %s, %s, NOW())',
                       [
                        param_dict.get('login_name'),
                        param_dict.get('name'),
                        password_md5])
        cursor.close()
        return const.ERRCODE_SUCC
    
    def doesAdminExist(self, db_conn, login_name, exclude_id=None):
        cursor = db_conn.cursor()
        sql_str_list = ["SELECT id FROM sys_user WHERE login_name=%s"]
        sql_var_list = [login_name]
        if exclude_id != None:
            sql_str_list.append("AND id!=%s")
            sql_var_list.append(exclude_id)
        
        cursor.execute(' '.join(sql_str_list), sql_var_list)
        t = cursor.fetchone()
        cursor.close()
        if t == None:
            return False
        return True
    
    def modifyAdminUser(self, db_conn, user_id, param_dict):
        cursor = db_conn.cursor()
        for k, v in param_dict.iteritems():
            cursor.execute('UPDATE sys_user SET ' + k +'=%s WHERE id=%s',
                           [v, user_id])
        cursor.execute('UPDATE sys_user SET last_login_time=NOW() WHERE id=%s',
                       [user_id])
        cursor.close()
        return const.ERRCODE_SUCC

    def modifyPassword(self, db_conn, user_id, param_dict):
        user_id = param_dict['id']
        cursor = db_conn.cursor()
        old_password_md5 = util.getMD5(param_dict['old_password'])
        cursor.execute('SELECT id FROM sys_user WHERE id=%s AND password=%s',
                       [user_id, old_password_md5])
        t = cursor.fetchone()
        if t == None:
            cursor.close()
            return const.ERRCODE_NO_SUCH_USER_OR_WRONG_PASSWORD
        
        new_password_md5 = util.getMD5(param_dict['password'])
        cursor.execute('UPDATE sys_user SET password=%s, last_login_time=NOW() WHERE id=%s',
                       [new_password_md5, user_id])
        cursor.close()
        return const.ERRCODE_SUCC
    
    # def deleteAdminUser(self, db_conn, user_id):
    #     cursor = db_conn.cursor()
    #     cursor.execute('UPDATE sys_user SET is_deleted=1,modify_time=NOW() WHERE id=%s', [user_id])
    #     cursor.close()
    #     return const.ERRCODE_SUCC
    


admin_user_svc = AdminUserService()
