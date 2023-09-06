from datetime import datetime

from sqlalchemy import Column, Integer, VARCHAR, SMALLINT, ForeignKey, \
    DateTime, Boolean, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.users.models import User

Base = declarative_base()


class Chat(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR, unique=True)
    status = Column(SMALLINT, nullable=False)
    updated_at = Column(SMALLINT, nullable=False)

    users = relationship("UserChat", back_populates="users")


class Message(Base):
    __tablename__ = "Message"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey(User.id))
    receiver_id = Column(Integer, ForeignKey(User.id))
    chat_id = Column(Integer, ForeignKey(Chat.id))
    text = Column(VARCHAR, nullable=False)
    time_delivered = Column(DateTime, default=datetime.now)
    time_seen = Column(DateTime, nullable=True)
    is_delivered = Column(Boolean, default=False)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])
    chat = relationship("Chat")


class UserChat(Base):
    __tablename__ = "user_chat"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey(Chat.id))
    user_id = Column(Integer, ForeignKey(User.id))

    chat = relationship("Chat", back_populates="users")
    user = relationship("User")

    __table_args__ = (
        UniqueConstraint("chat_id", "user_id", name="_chat_user_uc"),
    )
