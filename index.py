from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from src.routes import health, image, processes

load_dotenv()

app = FastAPI(
    title=os.getenv("app_name"),
    description=os.getenv("app_description"),
    version=os.getenv("app_version")
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(health.router, prefix="/v1")
app.include_router(image.router, prefix="/v1/images")

import uvicorn

from fastapi import Response

@app.get("/")
async def root():
    return {
        "status": "ok",
        "docs": "/docs",
        "health": "/v1/health"
    }

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)


if __name__ == "__main__":
    host = os.getenv("domain")
    if host == "localhost":
        host = "127.0.0.1"
    port = int(os.getenv("port"))
    uvicorn.run("index:app", host=host, port=port, reload=True)