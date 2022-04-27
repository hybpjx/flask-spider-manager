from flask import Flask, jsonify
from flask_cors import *
from flask_session import Session

from tutorial.user.user import user_bp
from tutorial.tianya.tianya import ty

app = Flask(__name__)

# app.register_blueprint()
app.config.from_pyfile('settings/dev.py')  # settings.py路径
CORS(app, supports_credentials=True)  # 全局结局跨域请求问题

Session(app)


# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(ty, url_prefix='/ty')

if __name__ == '__main__':
    app.run()
