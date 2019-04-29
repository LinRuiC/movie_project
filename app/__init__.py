#coding:utf8

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.redis import FlaskRedis
import os
import redis

app=Flask(__name__)
app.debug=True

# mysql数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/movie_project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# redis数据库配置
app.config["REDIS_HOST"] = "127.0.0.1"
app.config["REDIS_PORT"] = 6379

app.config['SECRET_KEY']='5eecf7cac4ac43e5af5343d2c4ecd228'
# 电影文件存放位置
app.config["MV_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/movie/")
# 会员文件 头像之类
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
# 电影预告
app.config["PR_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/preview/")
db=SQLAlchemy(app)
# rd = FlaskRedis(app)
rd = redis.StrictRedis(host=app.config["REDIS_HOST"], port=app.config["REDIS_PORT"])

from app.admin import admin_blueprint
from app.home import home
# 注册蓝图
app.register_blueprint(home)
app.register_blueprint(admin_blueprint,url_prefix='/admin')

# 自定义404错误页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'),404




