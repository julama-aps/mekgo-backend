from fastapi import APIRouter
from pymongo import MongoClient

from app.api.models.wc import WC


# TODO: URI & Name as Docker env vars
MONGODB_URI = "mongodb://0.0.0.0:27016"
DATABASE_NAME = "mekgo"

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

router = APIRouter()

@router.get("/")
def read_wcs():
    return {"message": "Read all items"}

@router.get("/{wc_id}")
def read_wc(wc_id: int):
    return {"message": f"Read item with ID: {wc_id}"}

@router.post("/insert_wc/")
def insert_item(wc: WC):
    collection = db.wcs
    inserted_wc = collection.insert_one(wc.dict())
    
    return {"inserted_id": str(inserted_wc.inserted_id)}