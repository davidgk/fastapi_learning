from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.api import router as api_router
from src.commons.configuration.database import Base, engine
from dotenv import load_dotenv
import os

def create_app():
    global app
    app = FastAPI()
    origins = [f'http://localhost:{os.getenv("PORT")}']
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router)
    Base.metadata.create_all(bind=engine)
    load_dotenv()
    return app
