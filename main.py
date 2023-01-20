import os

import uvicorn

from src.commons.configuration.create_app import create_app

app = create_app()

@app.get('/')
async def index():
    result = {"application": "FASTAPI POC"}
    return result

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=int(os.getenv("PORT")), log_level="info", reload=True)
    print("running")
