from fastapi import FastAPI
from datetime import datetime
import pytz

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tz = pytz.timezone("Africa/Lagos")


@app.get("/")
async def main():
    return {
        "email": "precious.eyoh999@gmail.com",
        "current_datetime": datetime.now(tz).isoformat(),
        "github_url": "https://github.com/Cyber-Freak999/HNG12-Task-0",
    }
