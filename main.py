import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.api import router as api_router
from src.commons.configuration.database import Base, engine

app = FastAPI()

origins = ["http://localhost:8005"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
Base.metadata.create_all(bind=engine)
@app.get('/')
async def index():
    result = {"application": "FASTAPI POC"}
    return result

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=3010, log_level="info", reload=True)
    print("running")

