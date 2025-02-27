"""Entrypoint of the API"""

from fastapi import FastAPI
from src.api import user, healthcheck, version
import uvicorn

app = FastAPI()

app.include_router(user.router)
app.include_router(healthcheck.router)
app.include_router(version.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000,reload=True)
