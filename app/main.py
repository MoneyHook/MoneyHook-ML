import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from app.api.predict import router as predict

load_dotenv()

app = FastAPI(
    title=os.getenv("API_TITLE", "FastAPI"), docs_url="/docs", redoc_url="/redoc"
)

app.include_router(predict, prefix="/api", tags=["Prediction"])


@app.get("/")
def root():
    return {"env": os.getenv("APP_ENV", "default")}


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
