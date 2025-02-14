
from datetime import datetime


class User:
    def __init__(self, username: str, hashed_password: str, user_id: int = None, is_admin: bool = False,
                 created_at: datetime | None = None):
        self.id = user_id
        self.username = username
        self.hashed_password = hashed_password
        self.is_admin = is_admin
        self.created_at = created_at or datetime.now()

    def __str__(self):
        return f"User(id={self.id}, username='{self.username}', is_admin={self.is_admin})"


class Todo:
    def __init__(self, todo_id, title, description, user_id):
        self.id = todo_id
        self.title = title
        self.description = description
        self.user_id = user_id

    def __str__(self):
        return f'Todo(ID: {self.id}, Title: {self.title}, Description: {self.description})'
