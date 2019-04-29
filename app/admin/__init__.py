from flask import Blueprint

# 创建蓝图
admin_blueprint=Blueprint('admin_blueprint',__name__)

# 导入视图函数  不加这句报错：找不到url
import app.admin.views