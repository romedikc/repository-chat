from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    photo_url: str

    class Config:
        orm_mode = True
