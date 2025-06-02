import hashlib
import sqlite3

DB_NAME = "users.db"


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def add_user(login: str, password: str, full_name: str) -> bool:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hashed = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)", (login, hashed, full_name))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    else:
        return True
    finally:
        conn.close()


def update_password(login: str, new_password: str) -> bool:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hashed = hash_password(new_password)
    cursor.execute("UPDATE users SET password = ? WHERE login = ?", (hashed, login))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0


def authenticate(login: str, password: str) -> bool:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE login = ?", (login,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return False
    stored_hash = row[0]
    return stored_hash == hash_password(password)


def main() -> None:
    while True:
        print("\n1. Add user  2. Update password  3. Authenticate  4. Exit")
        choice = input("> ").strip()
        if choice == "1":
            login = input("Login: ").strip()
            full_name = input("Full name: ").strip()
            pw = input("Password: ").strip()
            print("Added." if add_user(login, pw, full_name) else "User exists.")
        elif choice == "2":
            login = input("Login: ").strip()
            pw = input("New password: ").strip()
            print("Updated." if update_password(login, pw) else "User not found.")
        elif choice == "3":
            login = input("Login: ").strip()
            pw = input("Password: ").strip()
            print("Success." if authenticate(login, pw) else "Failed.")
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
