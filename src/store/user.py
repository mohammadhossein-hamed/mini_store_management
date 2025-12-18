# import json
from store.cart import Cart


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.purchase_history: list[
            dict[
                str,
                str
                | list[dict[str, dict[str, str | float | int] | int | float]]
                | float,
            ]
        ] = []

    def add_cart_to_history(self, cart: Cart):
        self.purchase_history.append(cart.to_dict())

    def to_dict(
        self,
    ) -> dict[
        str,
        str
        | list[
            dict[
                str,
                str
                | list[dict[str, dict[str, str | float | int] | int | float]]
                | float,
            ]
        ],
    ]:
        return {
            "username": self.username,
            "password": self.password,
            "purchase_history": self.purchase_history,
        }
