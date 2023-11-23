from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_wcs():
    return {"message": "Read all items"}

@router.get("/{wc_id}")
def read_wc(wc_id: int):
    return {"message": f"Read item with ID: {wc_id}"}
