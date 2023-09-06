from fastapi import APIRouter
from starlette import status

from src.chat.repository import ChatRepository
from src.chat.schemas import ChatSchema, UserChatSchema, MessageSchema
from src.database import session_maker

router = APIRouter(
    prefix="/chat",
    tags=["chats"]
)


@router.post("/create-chat/", status_code=status.HTTP_201_CREATED)
def create_chat(request: ChatSchema):
    with session_maker() as session:
        chat_repo = ChatRepository(session)
        chat = chat_repo.add_chat(
            name=request.name,
            status=request.status,
            updated_at=request.updated_at
        )
        session.commit()
        return {
            "id": chat.id,
            "name": chat.name,
            "status": chat.status,
            "updated_at": chat.updated_at
        }


@router.post("/create-user_chat/", status_code=status.HTTP_201_CREATED)
def create_user_chat(request: UserChatSchema):
    with session_maker() as session:
        user_chat_repo = ChatRepository(session)
        user_chat = user_chat_repo.add_user_chat(
            chat_id=request.chat_id,
            user_id=request.user_id,
        )
        session.commit()
        return {
            "id": user_chat.id,
            "chat_id": user_chat.chat_id,
            "user_id": user_chat.user_id,
        }


@router.post("/create_message/", status_code=status.HTTP_201_CREATED)
def create_message(request: MessageSchema):
    with session_maker() as session:
        message_repo = ChatRepository(session)
        message = message_repo.add_message(
            sender_id=request.sender_id,
            receiver_id=request.receiver_id,
            chat_id=request.chat_id,
            text=request.text,
            time_delivered=request.time_delivered,
            time_seen=request.time_seen,
            is_delivered=request.is_delivered
        )
        session.commit()
        return {
            "id": message.id,
            "sender_id": message.sender_id,
            "receiver_id": message.receiver_id,
            "chat_id": message.chat_id,
            "text": message.text,
            "time_delivered": message.time_delivered,
            "time_seen": message.time_seen,
            "is_delivered": message.is_delivered
        }


@router.get("/user-chats/", response_model=list[dict])
def get_user_сhats(user_id, status):
    with session_maker() as session:
        user_chat_repo = ChatRepository(session)
        user_chats = user_chat_repo.get_user_chats(user_id, status)
        return user_chats


@router.get("/messages/")
def get_messages(sender_id, receiver_id, time_delivered):
    with session_maker() as session:
        message_repo = ChatRepository(session)
        messages = message_repo.get_messages(sender_id, receiver_id, time_delivered)
        return messages
