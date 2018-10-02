from flask import Flask, render_template

from src.common.database import Database

app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "gblu098"

@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/')
def home():
    return render_template('home.html')


from src.models.users.views import user_blueprint
from src.models.sensors.views import sensor_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(sensor_blueprint, url_prefix='/sensors')