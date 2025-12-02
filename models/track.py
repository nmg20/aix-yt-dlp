from pydantic import BaseModel
from typing import Optional

class Track(BaseModel):
    title: str
    artist: Optional[str]
    album: Optional[str]
    duration: Optional[int]
    url: str