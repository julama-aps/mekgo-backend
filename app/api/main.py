from fastapi import FastAPI
from api.endpoints import wc


app = FastAPI()

app.include_router(wc.router, prefix="/wc", tags=["wc"])