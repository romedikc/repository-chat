from src.chat.models import Chat, UserChat, Message
from src.users.models import User


class ChatRepository:
    def __init__(self, session):
        self.session = session

    def get_user_chats(self, user_id: int, status: int = None):
        query = (
            self.session.query(Chat, UserChat, User)
            .join(UserChat, Chat.id == UserChat.chat_id)
            .join(User, User.id == UserChat.user_id)
            .filter(User.id == user_id)
        )

        if status:
            query = query.filter(Chat.status == status)

        user_chats = query.all()

        chat_data = []
        for chat, user_chat, user in user_chats:
            chat_data.append({
                "chat_id": chat.id,
                "chat_name": chat.name,
                "chat_status": chat.status,
                "updated_at": chat.updated_at,
                "user_id": user.id,
                "username": user.username,
            })

        return chat_data

    def get_messages(self, sender_id: int, receiver_id: int, time_delivered: int = None):
        query = self.session.query(Message)
        if sender_id:
            query = query.filter(Message.sender_id == sender_id)
        if receiver_id:
            query = query.filter(Message.receiver_id == receiver_id)
        if time_delivered:
            query = query.filter(Message.time_delivered == time_delivered)

        messages = query.first()
        return messages

    def add_chat(self, name: str, status: int, updated_at: int):
        chat = Chat(
            name=name,
            status=status,
            updated_at=updated_at
        )
        self.session.add(chat)
        return chat

    def add_user_chat(self, chat_id: int, user_id: int):
        user_chat = UserChat(
            chat_id=chat_id,
            user_id=user_id,
        )
        self.session.add(user_chat)
        return user_chat

    def add_message(self, sender_id: int, receiver_id: int, chat_id: int, text: str,
                    time_delivered: int, time_seen: int, is_delivered: bool):
        message = Message(
            sender_id=sender_id,
            receiver_id=receiver_id,
            chat_id=chat_id,
            text=text,
            time_delivered=time_delivered,
            time_seen=time_seen,
            is_delivered=is_delivered
        )
        self.session.add(message)
        return message
