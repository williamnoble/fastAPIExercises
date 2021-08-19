import json
import pathlib
from pathlib import Path

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

import weather_api
from weather_api.api import api
from weather_api.services import openweatherservice
from weather_api.views import home

app = fastapi.FastAPI()


def config():
    configure_api_keys()
    configure_routing()


def configure_api_keys():
    file: pathlib.Path = Path('settings.json').absolute()
    if not file.exists():
        print(f"Warning {file} not found")
        raise Exception("settings.json not found")

    with open('settings.json') as f:
        settings = json.load(f)
        openweatherservice.api_key = settings.get('api_key')


def configure_routing():
    app.mount("/static", StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(api.router)


if __name__ == '__main__':
    print('main')
    config()
else:
    config()
