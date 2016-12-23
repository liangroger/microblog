#coding=utf-8
from util import const


class ArticleService:
    def list_article(self, db_conn, param_dict, page, rows):
        page = int(page)
        rows = int(rows)

        where_list = ['del_flag=0']
        where_var_list = []

        if param_dict.get('category_id') != None:
            where_list.append('category_id=%s')
            where_var_list.append(param_dict['category_id'])

        cursor = db_conn.cursor()
        sql_str_list = ['SELECT COUNT(*) as count FROM cms_article']
        sql_var_list = []
        if len(where_list) > 0:
            sql_str_list.extend(['WHERE', ' AND '.join(where_list)])
            sql_var_list.extend(where_var_list)

        cursor.execute(' '.join(sql_str_list), sql_var_list)
        total = 0
        t = cursor.fetchone()
        if t is not None:
            total = int(t["count"])

        sql_str_list = ['SELECT id, category_id, title, link, image, keywords, description, content, update_date',
                        'FROM cms_article']
        sql_var_list = []
        if len(where_list) > 0:
            sql_str_list.extend(['WHERE', ' AND '.join(where_list)])
            sql_var_list.extend(where_var_list)
        sql_str_list.append('ORDER BY update_date DESC')

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

    def get_article(self, db_conn, entry_id):
        cursor = db_conn.cursor()
        sql_str_list = ['SELECT id,category_id, title, link, image, keywords, description, content, update_date, content',
                        'FROM cms_article',
                        'WHERE id=%s AND del_flag=0']
        cursor.execute(' '.join(sql_str_list), [entry_id])
        result = cursor.fetchone()
        cursor.close()
        return result

    def add_article(self, db_conn, param_dict):
        #new_id = str(uuid.uuid1()).replace('-', '')
        cursor = db_conn.cursor()
        cursor.execute('INSERT INTO cms_article(category_id, title, image, keywords, description, content,'
                       ' create_date, update_date) '
                       ' VALUES(%s, %s, %s, %s, %s, %s, NOW(), NOW())',
                       [param_dict.get('category_id'),
                        param_dict.get('title'),
                        param_dict.get('image'),
                        param_dict.get('keywords'),
                        param_dict.get('description'),
                        param_dict.get('content')])
        # get ID of last inserted record
        # print "ID of last record is ", int(cursor.lastrowid)  # 最后插入行的主键ID
        # print "ID of inserted record is ", int(db_conn.insert_id())  # 最新插入行的主键ID，conn.insert_id()一定要在conn.commit()之前，否则会返回0
        new_id = int(cursor.lastrowid)

        cursor.close()
        return const.ERRCODE_SUCC, new_id

    def modify_article(self, db_conn, entry_id, param_dict):
        #new_id = str(uuid.uuid1()).replace('-', '')
        cursor = db_conn.cursor()
        for k, v in param_dict.iteritems():
            cursor.execute('UPDATE cms_article SET ' + k +'=%s WHERE id=%s',
                           [v, entry_id])
        cursor.execute('UPDATE cms_article SET update_date=NOW() WHERE id=%s',
                       [entry_id])
        cursor.close()
        return const.ERRCODE_SUCC

    def delete_article(self, db_conn, entry_id):
        cursor = db_conn.cursor()
        cursor.execute('UPDATE cms_article SET del_flag=1,update_date=NOW() WHERE id=%s', [entry_id])
        cursor.close()
        return const.ERRCODE_SUCC

article_srv = ArticleService()