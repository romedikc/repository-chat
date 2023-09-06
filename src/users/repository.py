from src.users.models import User


class UsersRepository:
    def __init__(self, session):
        self.session = session

    def get(self, id: int, username: str):
        query = self.session.query(User)
        if id:
            query = query.filter(User.id == id)
        if username:
            query = query.filter(User.username == username)

        user = query.first()
        return user

    def list(self):
        return self.session.query(User).all()

    def add(self, username: str, photo_url: str):
        user = User(
            username=username,
            photo_url=photo_url
        )
        self.session.add(user)
        return user
