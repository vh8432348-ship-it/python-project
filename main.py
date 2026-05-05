# # Завдання 1
#
#
from fastapi import FastAPI

#
# app = FastAPI()
#
#
# @app.post("/hello")
# def hello():
#     return {"message": "Привіт з сервера!"}
# Завдання 2


app = FastAPI()


@app.get("/greeting")
def greeting():
    return {"respond": "Привіт з сервера1"}
