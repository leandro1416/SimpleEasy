from fastapi import FastAPI, Query

from src.app import greet_localized, greet_time_based

app = FastAPI(title="SimpleEasy API")


@app.get("/hello")
def hello(
    name: str = Query("world", min_length=1),
    lang: str = Query("en"),
    time: bool = Query(False, alias="time"),
):
    if time:
        return {"message": greet_time_based(name, lang)}
    return {"message": greet_localized(name, lang)}
