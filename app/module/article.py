#coding=utf-8

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

        sql_str_list = ['SELECT id, category_id, title, link, image, keywords, description, update_date',
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

    def getArticleEntry(self, db_conn, entry_id):
        cursor = db_conn.cursor()
        sql_str_list = ['SELECT cms_article.id,category_id, title, link, image, keywords, description, update_date, content',
                        'FROM cms_article',
                        'LEFT JOIN cms_article_data on cms_article.id=cms_article_data.id',
                        'WHERE cms_article.id=%s AND del_flag=0']
        cursor.execute(' '.join(sql_str_list), [entry_id])
        result = cursor.fetchone()
        cursor.close()
        return result

article_srv = ArticleService()