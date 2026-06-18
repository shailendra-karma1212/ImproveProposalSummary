from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Summary Improvement Agent",
    version="1.0.0"
)

app.include_router(router)