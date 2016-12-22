#coding=utf-8

class CategoryService:
    def getCategoryList(self,db_conn,parent_id):
        cursor = db_conn.cursor()
        sql_str_list = ['SELECT id, parent_id, name, in_menu, in_list  FROM cms_category WHERE parent_id=%s']
        cursor.execute(' '.join(sql_str_list), [parent_id])
        result = cursor.fetchall()
        cursor.close()
        return result

category_srv = CategoryService()