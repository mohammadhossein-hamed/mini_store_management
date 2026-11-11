import getpass
from .database import get_users, save_users
from .user import User


def get_input():
    username = input("\nUsername:")
    password = getpass.getpass("Password:")
    return username, password


def login():
    username, password = get_input()
    data = get_users()
    for user in data:
        if username == user["username"]:  # type: ignore
            if password == user["password"]:  # type: ignore
                return username, "\n✅ Login, successful! Welcome.\n"
            else:
                return "", "\n❌ Password is wrong.\n"

    return "", "\n❕ Username not found.\n"


def signup():
    username, password = get_input()

    data = get_users()
    for user in data:
        if username == user["username"]:  # type: ignore
            return "", "❗️ Username is taken, please choose another one."

    new_user = User(username, password).to_dict()
    data.append(new_user)  # type: ignore
    save_users(data)  # type: ignore

    return username, "💎 Signed up Seccessfully!"
