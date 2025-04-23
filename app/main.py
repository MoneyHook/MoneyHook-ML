from fastapi import FastAPI
from dotenv import load_dotenv
import os

import uvicorn

load_dotenv()

app = FastAPI(title=os.getenv("API_TITLE", "FastAPI"))


@app.get("/")
def read_root():
    print("hej")
    return {"env": os.getenv("APP_ENV", "default")}


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
