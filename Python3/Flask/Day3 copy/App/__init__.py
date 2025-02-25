# MVC
from flask import Flask
from .setting import envs
from .ext import init_ext
from .views import init_view
# 数据库模型导入使其在flask_migrate扩展中使用
from .models import User,Member

def create_app(env):
  # 获取Flask-APP对象
  app = Flask(__name__)

  # 应用配置加载
  app.config.from_object(envs.get(env))

  # 初始化扩展
  init_ext(app)

  # 初始化路由蓝图
  init_view(app=app)

  return app
