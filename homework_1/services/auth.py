import hashlib
import secrets

from models.users import User
from repositories import UserRepository
from schemas import LoginUser, RegisterUser


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, user_data: RegisterUser) -> User | None:
        existing_user = self.repository.get_user_by_username(user_data.username)
        if existing_user is not None:
            return None

        password_hash = self._hash_password(user_data.password)
        return self.repository.create_user(user_data.username, password_hash)

    def login(self, credentials: LoginUser) -> str | None:
        user = self.repository.get_user_by_username(credentials.username)
        if user is None:
            return None

        password_hash = self._hash_password(credentials.password)
        if user.password_hash != password_hash:
            return None

        access_token = secrets.token_urlsafe(32)
        self.repository.set_access_token(user, access_token)
        return access_token

    def get_user_by_token(self, access_token: str) -> User | None:
        return self.repository.get_user_by_token(access_token)

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
