from fastapi import APIRouter, Body, HTTPException, status

import motor.motor_asyncio
from bson import ObjectId
from pymongo import ReturnDocument
from fastapi.responses import Response

from app.api.models.wc import WCModel, UpdateWCModel, WCCollection


# TODO: URI & Name as Docker env vars
MONGODB_URI = "mongodb://192.168.1.33:27016"
DATABASE_NAME = "mekgo"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client.mekgo
wcs_collection = db.get_collection("wcs")

router = APIRouter()

#### CRUD ####
## Create ##
# Post WC
@router.post(
    "/new/",
    response_description="Add new wc",
    response_model = WCModel,
    status_code = status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_wc(wc: WCModel = Body(...)):
    new_wc = await wcs_collection.insert_one(
        wc.model_dump(by_alias=True, exclude=["id"])
    )
    created_wc = await wcs_collection.find_one(
        {"_id": new_wc.inserted_id}
    )
    return created_wc

## Read ##
# Get All WCs
@router.get(
    "/",
    response_description="List all wcs",
    response_model=WCCollection,
    response_model_by_alias=False,
)
async def list_wcs():
    return WCCollection(wcs=await wcs_collection.find().to_list(1000))

# Get Specific WC
@router.get(
    "/{id}",
    response_description="Get a single wc",
    response_model=WCModel,
    response_model_by_alias=False,
)
async def show_wc(id: str):
    if (
        wc := await wcs_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return wc

    raise HTTPException(status_code=404, detail=f"WC {id} not found")

## Update ##
# Update Specific WC
@router.put(
    "/update/{id}",
    response_description="Update a wc",
    response_model=WCModel,
    response_model_by_alias=False,
)
async def update_wc(id: str, wc: UpdateWCModel = Body(...)):
    wc = {
        k: v for k, v in wc.model_dump(by_alias=True).items() if v is not None
    }

    if len(wc) >= 1:
        update_result = await wcs_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": wc},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"WC {id} not found")

    # The update is empty, but we should still return the matching document:S
    if (existing_wc := await wcs_collection.find_one({"_id": id})) is not None:
        return existing_wc

    raise HTTPException(status_code=404, detail=f"WC {id} not found")

## Delete ##
# Delete Specific WC
@router.delete("/{id}", response_description="Delete a WC")
async def delete_wc(id: str):
    delete_result = await wcs_collection.delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"WC {id} not found")