from pydantic import BaseModel


# TODO: Handle _id ObjectId from MongoDB
class WC(BaseModel):
    title: str
    comment: str
    location: str
    photo: str
    rating: int
