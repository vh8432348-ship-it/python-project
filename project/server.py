from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

FILE_NAME = "films.json"


class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int


def load_movies():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_movies(movies):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(movies, file, ensure_ascii=False, indent=4)


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    movies = load_movies()

    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    raise HTTPException(status_code=404, detail="Фільм не знайдено")


@app.post("/movies")
def add_movie(movie: Movie):
    movies = load_movies()

    for m in movies:
        if m["id"] == movie.id:
            raise HTTPException(status_code=400, detail="ID вже існує")

    movies.append(movie.dict())
    save_movies(movies)

    return {"message": "Фільм додано"}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    movies = load_movies()

    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            save_movies(movies)

            return {"message": "Фільм видалено"}

    raise HTTPException(status_code=404, detail="Фільм не знайдено")
