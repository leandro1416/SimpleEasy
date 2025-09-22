import asyncio

import httpx
import pytest
import uvicorn


async def _run_server():
    config = uvicorn.Config("src.server:app", host="127.0.0.1", port=8001, log_level="error")
    server = uvicorn.Server(config)
    task = asyncio.create_task(server.serve())
    # Wait briefly for startup
    await asyncio.sleep(0.2)
    return server, task


async def _stop_server(server, task):
    server.should_exit = True
    await task


@pytest.mark.asyncio
async def test_hello_basic():
    server, task = await _run_server()
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get("http://127.0.0.1:8001/hello", params={"name": "Alice"})
            assert r.status_code == 200
            assert r.json()["message"] == "Hello, Alice!"
    finally:
        await _stop_server(server, task)


@pytest.mark.asyncio
async def test_hello_time_pt():
    server, task = await _run_server()
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(
                "http://127.0.0.1:8001/hello", params={"name": "Ana", "lang": "pt", "time": "true"}
            )
            assert r.status_code == 200
            # We don't control the hour here, but the response should be non-empty and contain name
            assert "Ana" in r.json()["message"]
    finally:
        await _stop_server(server, task)


@pytest.mark.asyncio
async def test_health_ready():
    server, task = await _run_server()
    try:
        async with httpx.AsyncClient() as client:
            rh = await client.get("http://127.0.0.1:8001/health")
            rr = await client.get("http://127.0.0.1:8001/ready")
            assert rh.status_code == 200 and rr.status_code == 200
            assert rh.json()["status"] == "ok"
            assert rr.json()["status"] == "ready"
    finally:
        await _stop_server(server, task)
