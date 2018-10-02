import datetime
import uuid

from src.common.database import Database
import src.models.sensors.constants as SensorConstants


class Sensor_DHT(object):
    def __init__(self, temperature, humidity, last_checked=None, _id=None):
        self.temperature = float(temperature)
        self.humidity = float(humidity)
        self.last_checked = datetime.datetime.utcnow() if last_checked is None else last_checked
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Sensor data for temperature: {} and humidity: {} on {}>".format(self.temperature, self.humidity, self.last_checked)

    def json(self):
        return {
            "_id": self._id,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "last_checked": self.last_checked
        }

    def save_to_db(self):
        Database.insert(SensorConstants.COLLECTION_DHT, self.json())

    @classmethod
    def get_from_db(cls):
        return [cls(**data) for data in Database.find(SensorConstants.COLLECTION_DHT, {})]