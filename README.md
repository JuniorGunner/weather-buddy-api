# Weather Buddy API

<img align="right" width="120" src="img/devgrid.png">

## About this application

An Rest API to perform weather requests with the OpenWeatherMap API, developed with the objective of fix the need raised by the initial challenge of the selection process for back-end developer of **[DevGrid](https://devgrid.co.uk)**.

## Run the application with Docker

To run this project in a simple way, it's necessary that you have **Docker** in the version >= 19 and **Docker Compose** in the version >= 1.25 installed on your machine.

1. First, clone the remote application repository on your local machine:

 ```bash
 $ git clone git@github.com:JuniorGunner/weather-buddy-api.git
 ```

2. Then, access the application's base directory:

 ```bash
 $ cd weather-buddy-api
 ```

3. Finally, being in the directory, just build and up a container with the application in Flask:

 ```bash
 $ docker-compose up --build
 ```

**Ready!** The Rest API is available on your local machine on the URL `http://localhost:5000/`

## Services available in the application

As requested by the initial challenge, the application consists of a set of microservices for to perform weather requests with the OpenWeatherMap API in JSON format.

The application provides a service interface mapped below:

### Index

It's a small initial interface that returns a message of greetings. If you can see it **"Hello, DevGrid!"**, it means that the application is fully operational.

**GET** `http://localhost:5000/` *Get the main page greeting*

- **Parameters**

  This endpoint has no input parameters.

- **Response**

  This is the result for `http://localhost:5000`:

  ```json
  {
    "greeting": "Hello, DevGrid!"
  }
  ```

### Weather

It's the main interface of the application. It's responsible for providing the Weather management functionality. From this interface, we can request the weather in cities.

**GET** `http://localhost:5000/temperature/<city_name>` *get a city weather*

- **Parameters**

  This endpoint has no input parameters.

- **Responses**

  This is the result for `http://localhost:5000/temperature/Los Angeles`:

  ```json
  {
    "min": 17.76,
    "max": 31.44,
    "avg": 24.7,
    "feels_like": 24.71,
    "city": "Los Angeles",
    "country": "US"
  }
  ```
  > Once requested, this city will be available for 5 minutes in cache.

**GET** `http://localhost:5000/temperature` *get a list of weathers in cache*

- **Parameters**

  |key|description|type|required|
  |-|-|-|-|
  |`max`|Define the number of cities to be request. This parameter must be a positive integer between 1 and 5. Ex.: `4`. If not informed, the default value will be `5`|integer|**no**|

- **Responses**

  This is the result for `http://localhost:5000/temperature?max=4`:

  ```json
  [
  {
    "min": 17.76,
    "max": 31.44,
    "avg": 24.7,
    "feels_like": 24.71,
    "city": "Los Angeles",
    "country": "US"
  },
  {
    "min": 25.02,
    "max": 25.02,
    "avg": 25.02,
    "feels_like": 26.03,
    "city": "Belém",
    "country": "BR"
  },
  {
    "min": 7.86,
    "max": 12.82,
    "avg": 10.02,
    "feels_like": 8.54,
    "city": "Toronto",
    "country": "CA"
  },
  {
    "min": 21.2,
    "max": 23.03,
    "avg": 21.66,
    "feels_like": 22.28,
    "city": "São Paulo",
    "country": "BR"
  }
]
  ```

## For Developers

### Settings environment

To configure your development environment, it's necessary that you have **Pipenv** installed on your machine.

1. First, clone the remote application repository on your local machine:

 ```bash
 $ git clone git@github.com:JuniorGunner/weather-buddy-api.git
 ```

2. Them, access the application's base directory:

 ```bash
 $ cd weather-buddy-api
 ```

3. Now, create a `.env` environment configuration file in the base directory with the following content:

 ```env
 # Flask App settings
 FLASK_APP=api
 FLASK_ENV=development
 DEBUG=True

 # OpenWeatherMap API settings
 OPENWEATHERMAP_TOKEN=3f62164f8ce1f8cb5ae8e2d02918babb
 ```
 > **Note:** In the `.env` file there are configuration variables for the flask application and authentication in the OpenWeatherMap API. The `OPENWEATHERMAP_TOKEN` variable is receiving a default value that is an access token generated exclusively for this public application. But, feel free to generate your own access token at the [OpenWeatherMap Official Website](https://openweathermap.org) and use it, if desired.

### Run the application

Assuming that the previous step was properly performed, to run the application in development mode, just follow the guidelines below:

1. First, install required packages with Pipenv:

 ```bash
 $ pipenv install
 ```

2. Finally, run the application with Flask:

 ```bash
 $ pipenv run flask run
 ```

 > **Note:** All commands related to a python environment, such as `pip freeze` or `python [file]`, are available, using the `pipenv run` command as a prefix to run any command within the environment.

### Test the application with Pytest

Assuming that the "Settings environment" step was properly executed, to run the application tests in development mode, just follow the guidelines below:

1. First, install development required packages:

 ```bash
 $ pipenv install --dev
 ```

 > **Note:** This command installs all packages installed in the previous example, also including development packages listed in `[dev-packages]` in the `Pipfile`.

2. Finally, run the application tests with Pytest:

 ```bash
 $ pipenv run pytest
 ```
