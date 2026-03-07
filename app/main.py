from fastapi import FastAPI
from app.core import router as core_router
from app.user_app import router as user_router

def create_app() -> FastAPI:
    app = FastAPI(title="DevOps Practice App")

    # Stable DevOps endpoints
    app.include_router(core_router)

    # Tutorial endpoints under /app/*
    app.include_router(user_router, prefix="/app")

    return app

app = create_app()