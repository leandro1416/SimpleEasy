import json
import logging
import os
import time

from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware

from src.app import greet_localized, greet_time_based

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("simpleeasy")

app = FastAPI(title="SimpleEasy API")

# CORS: allow local dev and any origins from APP_CORS_ORIGINS (comma-separated)
default_origins = ["http://localhost:5173", "http://127.0.0.1:5173"]
extra_origins = [o.strip() for o in os.getenv("APP_CORS_ORIGINS", "").split(",") if o.strip()]
allow_origins = default_origins + extra_origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def access_log(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration_ms = int((time.time() - start) * 1000)
    fmt = os.getenv("APP_LOG_FORMAT", "json").lower()
    if fmt == "plain":
        logger.info(
            "%s %s -> %s (%dms)",
            request.method,
            request.url.path,
            response.status_code,
            duration_ms,
        )
    else:
        log = {
            "level": "info",
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "duration_ms": duration_ms,
        }
        logger.info(json.dumps(log, ensure_ascii=False))
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
