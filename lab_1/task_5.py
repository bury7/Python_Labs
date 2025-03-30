import hashlib
from getpass import getpass


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode("utf-8"), usedforsecurity=False).hexdigest()


def verify_user(login: str, password: str, users: list[dict[str, str]]) -> bool:
    return login in users and hash_password(password) == users[login]["password"]


def print_heading(title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))


def main() -> None:
    users = {
        "admin": {
            "password": hash_password("admin123"),
            "name": "System Administrator",
        },
        "artem": {
            "password": hash_password("qwerty"),
            "name": "Nizhyvenko Artem Dmytrovych",
        },
        "user": {
            "password": hash_password("securepass"),
            "name": "Just Some User",
        },
    }

    print_heading("User Login")
    login = input("Enter login: ")
    password = getpass("Enter password: ")

    if verify_user(login, password, users):
        print(f"Welcome, {users[login]['name']}!")
    else:
        print("Invalid login or password!")


if __name__ == "__main__":
    main()
