from fastapi import APIRouter
from pymongo import MongoClient

from app.api.models.wc import WC


# TODO: URI & Name as Docker env vars
MONGODB_URI = "mongodb://192.168.1.33:27016"
DATABASE_NAME = "mekgo"

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
collection = db['wcs']

router = APIRouter()

#### CRUD ####
## Create ##
# Post WC
@router.post("/new")
def insert_wc(wc: WC):
    inserted_wc = collection.insert_one(wc.dict())
    return {"inserted_id": str(inserted_wc.inserted_id)}

## Read ##
# Get All WCs
@router.get("/")
def read_wcs():
    return {"message": "Read all items"}

# Get Specific WC
@router.get("/{wc_id}")
def read_wc(wc_id: str):
    return {"message": f"Read wc with ID: {wc_id}"}

## Update ##
# Update Specific WC
@router.put("/modify/{wc_id}")
def modify_wc(wc_id: str):
    return {"message": f"Modify wc with ID: {wc_id}"}

## Delete ##
# Delete Specific WC
@router.delete("/delete/{wc_id}")
def delete_wc(wc_id: str):
    return {"message": f"Delete wc with ID: {wc_id}"}