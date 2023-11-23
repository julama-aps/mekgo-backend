from fastapi import FastAPI
from src.api.v1.endpoints import wc


app = FastAPI()

app.include_router(wc.router, prefix="/wc", tags=["wc"])