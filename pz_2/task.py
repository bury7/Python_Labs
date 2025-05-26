import datetime as dt
import hashlib


class User:
    def __init__(self, username: str, password: str, is_active: bool = True) -> None:  # noqa: FBT001, FBT002
        self.username = username
        self.password_hash = self._hash_password(password)
        self.is_active = is_active

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str) -> bool:
        return self.password_hash == self._hash_password(password)


class AccessControl:
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, user: User) -> None:
        self.users[user.username] = user

    def authenticate_user(self, username: str, password: str) -> User | None:
        user = self.users.get(username)
        if user and user.verify_password(password) and user.is_active:
            return user
        return None


class Administrator(User):
    def __init__(
        self,
        username: str,
        password: str,
        access_control: AccessControl,
        permissions: list[str] | None = None,
    ) -> None:
        super().__init__(username, password)
        self.access_control = access_control
        self.permissions = permissions if permissions is not None else []

    def add_permission(self, permission: str) -> None:
        if permission not in self.permissions:
            self.permissions.append(permission)

    def add_user_to_system(self, user: User) -> None:
        self.access_control.add_user(user)
        print(f"Administrator {self.username} added user: {user.username}")

    def authenticate_any_user(self, username: str, password: str) -> User | None:
        return self.access_control.authenticate_user(username, password)


class RegularUser(User):
    def __init__(self, username: str, password: str, last_login: dt.datetime | None = None) -> None:
        super().__init__(username, password)
        self.last_login = last_login

    def update_last_login(self) -> None:
        self.last_login = dt.datetime.now(tz=dt.UTC)


class GuestUser(User):
    def __init__(self, username: str) -> None:
        super().__init__(username, password="", is_active=False)

    def verify_password(self, _password: str) -> bool:
        return False


if __name__ == "__main__":
    ac = AccessControl()

    admin = Administrator("admin", "admin", access_control=ac)
    ac.add_user(admin)

    user = RegularUser("alice", "qwerty")
    admin.add_user_to_system(user)

    guest = GuestUser("guest")
    admin.add_user_to_system(guest)

    user_auth = admin.authenticate_any_user("alice", "qwerty")
    print("Alice auth:", "OK" if user_auth else "FAIL")

    wrong_auth = admin.authenticate_any_user("alice", "wrong")
    print("Wrong password:", "BLOCKED" if wrong_auth is None else "ERROR")

    guest_auth = admin.authenticate_any_user("guest", "any")
    print("Guest auth:", "BLOCKED" if guest_auth is None else "ERROR")
