from flask import Flask
from flask_restful import Api
from flask_caching import Cache

# Create and configure Flask App instance
app = Flask(__name__)

# Create and configure Flask Cache instance
cache = Cache(app, config={'CACHE_TYPE': 'flask_caching.backends.SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})
cache.init_app(app)

# Create a Flask RESTful Api instance
api = Api(app)

# Import Api endpoints
from api.resources.index import IndexView
from api.resources.weather import WeatherListView, WeatherView

# Add Api endpoints
api.add_resource(IndexView, '/', endpoint='index')
api.add_resource(WeatherListView, '/temperature', endpoint='weather_list')
api.add_resource(WeatherView, '/temperature/<string:city_name>', endpoint='weather')
