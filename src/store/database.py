import json
from pathlib import Path


current_dir = Path(__file__).parent.parent.parent
products_josn = current_dir / "data" / "products.json"
users_json = current_dir / "data" / "users.json"


def get_products():
    return load_json(products_josn)


def get_users():
    return load_json(users_json)


def save_products(data: json):  #type: ignore
    dump_json(products_josn, data)


def save_users(data: json):     #type: ignore
    dump_json(users_json, data)


def load_json(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return "File not found !"


def dump_json(file_path: Path, data):  # type: ignore

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    get_products()
    get_users()
