# coding=utf-8
import logging


#### SERVER ####
SERVER_PORT = 10010
SERVER_HOST = '127.0.0.1'

##### LOG #####
LOG_PATH = './log/'
LOG_LEVEL = logging.DEBUG

##### MYSQL #####
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = '123456'
DBNAME = 'micro_cms'
DB_POOL_SIZE = 5


##### ADMIN ACCOUNT MYSQL #####
ADMIN_DB_HOST = 'localhost'
ADMIN_DB_PORT = 3306
ADMIN_DB_USER = 'root'
ADMIN_DB_PASSWORD = '123456'
ADMIN_DBNAME = 'micro_cms'
ADMIN_DB_POOL_SIZE = 5


##### FLASK LOGIN #####
SECRET_KEY = '\x10\xa3\x08\x85\xca\xa1\x4b\x34\x10\x73\xf1\xc3\xbc'

