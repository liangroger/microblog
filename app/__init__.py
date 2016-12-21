#encoding=utf-8
from flask import Flask
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

if not app.debug:
    file_handler = RotatingFileHandler('../tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

## 注册http接口请求
from app import views