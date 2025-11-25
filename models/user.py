import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


class User:
    def __init__(self, id, username, password, email, role):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.role = role

    def __repr__(self):
        return (
            f"User(id={self.id}, username='{self.username}', "
            f"email='{self.email}', role='{self.role}')"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "role": self.role
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            username=data["username"],
            password=data["password"],
            email=data["email"],
            role=data["role"]
        )


class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, "users.json")

    def __init__(self):
        self.users = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [User.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(
                [u.to_dict() for u in self.users],
                f,
                indent=4,
                ensure_ascii=False
            )

    def get_all(self):
        return self.users

    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)

    def add_user(self, user: User):
        self.users.append(user)
        self._save()

    def update_user(self, updated_user: User):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break

    def delete_user(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()
