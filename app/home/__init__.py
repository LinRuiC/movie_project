from flask import Blueprint

# 创建蓝图
home=Blueprint('home',__name__)

# 导入视图函数 不加这句报错：找不到url
import app.home.views

