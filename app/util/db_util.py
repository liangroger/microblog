#coding=utf-8

import MySQLdb
from MySQLdb import cursors
from DBUtils.PooledDB import PooledDB

g_db_pool = None

def getConnection(config):
    global g_db_pool
    if g_db_pool == None:
        g_db_pool = PooledDB(MySQLdb,
                             5,
                             host=config.DB_HOST,
                             port=config.DB_PORT,
                             user=config.DB_USER,
                             passwd=config.DB_PASSWORD,
                             db=config.DBNAME,
                             cursorclass = cursors.DictCursor,
                             charset="utf8")
    conn = g_db_pool.connection()
    cursor = conn.cursor()
    cursor.execute("set names utf8mb4;")
    cursor.close()
    return conn


g_admin_db_pool = None

def getAdminDBConnection(config):
    import MySQLdb
    from MySQLdb import cursors
    from DBUtils.PooledDB import PooledDB
    
    global g_admin_db_pool
    if g_admin_db_pool == None:
        g_admin_db_pool = PooledDB(MySQLdb,
                                   5,
                                   host=config.ADMIN_DB_HOST,
                                   port=config.ADMIN_DB_PORT,
                                   user=config.ADMIN_DB_USER,
                                   passwd=config.ADMIN_DB_PASSWORD,
                                   db=config.ADMIN_DBNAME,
                                   cursorclass = cursors.DictCursor,
                                   charset='utf8')
    conn = g_admin_db_pool.connection()
    cursor = conn.cursor()
    cursor.execute("set names utf8mb4;")
    cursor.close()
    return conn
