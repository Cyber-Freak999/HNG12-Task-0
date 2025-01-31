from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
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
    data = {
        "email": "precious.eyoh999@gmail.com",
        "current_datetime": datetime.now(tz).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Cyber-Freak999/HNG12-Task-0"
    }
    
    formatted_response = jsonable_encoder(data)
    return JSONResponse(content=formatted_response, media_type="application/json")
