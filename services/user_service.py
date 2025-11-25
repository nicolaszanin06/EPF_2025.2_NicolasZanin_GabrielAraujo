from bottle import request
from models.user import UserModel, User

class UsersService:
    def __init__(self):
        self.model = UserModel()

    def list_all(self):
        return self.model.get_all()

    def get_by_id(self, user_id: int):
        return self.model.get_by_id(user_id)

    def find_by_username(self, username: str):
        users = self.model.get_all()
        return next((u for u in users if u.username == username), None)

    def save(self):
        users = self.model.get_all()
        last_id = max((u.id for u in users), default=0)
        new_id = last_id + 1

        username = request.forms.get('username')
        password = request.forms.get('password')
        email = request.forms.get('email')

        user = User(id=new_id, username=username, password_hash=password, email=email)

        self.model.add_user(user)

    def update(self, user: User):
        user.username = request.forms.get('username')
        user.password_hash = request.forms.get('password')
        user.email = request.forms.get('email')

        self.model.update_user(user)

    def delete(self, user_id: int):
        self.model.delete_user(user_id)
