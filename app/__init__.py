from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, template_folder='static/templates')
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views