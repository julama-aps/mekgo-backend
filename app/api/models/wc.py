from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator

from typing import Optional, List
from typing_extensions import Annotated

from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(str)]    

class WCModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(...)
    comment: str = Field(...)
    location: str = Field(...)
    photo: str = Field(...)
    rating: float = Field(..., le=5.0)
    model_config = ConfigDict(
        populate_by_name = True,
        arbitrary_types_allowed = True,
        json_schema_extra = {
            "example": {
                "title": "Renfe",
                "comment": "Limpio de cojones y con pestillo.",
                "location": "Coordenadas",
                "photo": "String en Base64",
                "rating": 4.7,
            }
        },
    )

class UpdateWCModel(BaseModel):
    title: Optional[str] = None
    comment: Optional[str] = None
    location: Optional[str] = None
    photo: Optional[str] = None
    rating: Optional[float] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders = {ObjectId: str},
        json_schema_extra = {
            "example": {
                "title": "Renfe",
                "comment": "Limpio de cojones y con pestillo.",
                "location": "Coordenadas",
                "photo": "String en Base64",
                "rating": 4.7,
            }
        },
    )


class WCCollection(BaseModel):
    wcs: List[WCModel]