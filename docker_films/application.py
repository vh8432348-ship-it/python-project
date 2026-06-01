import json

from fastapi import FastAPI

from settings import settings

app = FastAPI()


@app.get("/films")
def get_films():
    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        films = json.load(file)

    if settings.max_films:
        films = films[: settings.max_films]

    return films
