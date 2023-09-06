from fastapi import APIRouter, HTTPException
from starlette import status

from src.users.repository import UsersRepository
from src.users.schemas import UserSchema
from src.database import session_maker

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/all-users/")
def get_users():
    with session_maker() as session:
        user_repo = UsersRepository(session)
        users = user_repo.list()
        return {
            "users": users
        }


@router.get("/user_id/")
def get_user(id: int = None, username: str = None):
    with session_maker() as session:
        user_repo = UsersRepository(session)
        user = user_repo.get(id=id, username=username)
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден!")
        return user


@router.post("/create-user/", status_code=status.HTTP_201_CREATED)
def create_user(request: UserSchema):
    with session_maker() as session:
        user_repo = UsersRepository(session)
        user = user_repo.add(
            username=request.username,
            photo_url=request.photo_url
        )
        session.commit()
        return {
            "id": user.id,
            "username": user.username,
            "photo_url": user.photo_url
        }
