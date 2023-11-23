from pydantic import BaseModel


# TODO: Location real data
class WC(BaseModel):
    title: str
    comment: str
    location: str
    photo: str
    rating: int
