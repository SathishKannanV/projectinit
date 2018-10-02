from flask import Blueprint, render_template, request, url_for, redirect

from src.models.sensors.sensor1 import Sensor_DHT
import src.models.users.decorators as user_decorator

sensor_blueprint = Blueprint('sensors', __name__)

@sensor_blueprint.route('/')
def index():
    sensors = Sensor_DHT.get_from_db()
    return render_template('sensors/sensor_index.html', sensors=sensors)

@sensor_blueprint.route('/sensor_dht')
def sensor_dht_page():
    sensors = Sensor_DHT.get_from_db()
    return render_template('sensors/sensor_dht_home.html', sensors=sensors)

@sensor_blueprint.route('/sensor_dht/getdata', methods=['GET'])
def get_sensor_data():
    temperature = request.args.get('temperature')
    humidity = request.args.get('humidity')
    data = Sensor_DHT(temperature, humidity)
    data.save_to_db()
    return "Sensor data recorded"


