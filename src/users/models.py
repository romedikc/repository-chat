from datetime import datetime

from sqlalchemy import Column, Integer, VARCHAR, SMALLINT, ForeignKey, DateTime, Boolean, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR, unique=True, nullable=False)
    photo_url = Column(VARCHAR, nullable=True)
