import logging

from fastapi import FastAPI, Query, Request

from src.app import greet_localized, greet_time_based

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("simpleeasy")

app = FastAPI(title="SimpleEasy API")


@app.middleware("http")
async def access_log(request: Request, call_next):
    path = request.url.path
    method = request.method
    response = await call_next(request)
    logger.info("%s %s -> %s", method, path, response.status_code)
    return response


@app.get("/hello")
def hello(
    name: str = Query("world", min_length=1),
    lang: str = Query("en"),
    time: bool = Query(False, alias="time"),
):
    if time:
        return {"message": greet_time_based(name, lang)}
    return {"message": greet_localized(name, lang)}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    # place to add future checks (e.g., DB connectivity)
    return {"status": "ready"}
