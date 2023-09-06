from datetime import datetime

from pydantic import BaseModel


class ChatSchema(BaseModel):
    name: str
    status: int
    updated_at: int


class MessageSchema(BaseModel):
    sender_id: int
    receiver_id: int
    chat_id: int
    text: str
    time_delivered: datetime
    time_seen: datetime
    is_delivered: bool

    class Config:
        orm_mode = True


class UserChatSchema(BaseModel):
    chat_id: int
    user_id: int
    is_sender: bool

    class Config:
        orm_mode = True
