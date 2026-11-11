import secrets
import base64

from .cart_item import CartItem
from .product import Product


class Cart:
    def __init__(self) -> None:
        self.cart_id = (
            base64.urlsafe_b64encode(secrets.token_bytes(9)).decode().rstrip("=")
        )
        self.items: list[CartItem] = []


    def add_to_cart(self, prduct: Product, quantity: int = 1):
        item = CartItem(prduct, quantity)
        self.items.append(item)

    def remove_from_cart(self, item_num: int, quantity: int = 1):

        self.items[item_num].quantity -= quantity
        if self.items[item_num].quantity == 0:
            self.items.remove(self.items[item_num])

    def view_cart(self):
        return [item for item in self.items]

    def total_price_cart(self) -> float:
        return sum([item.total_price_item() for item in self.items])

    def to_dict(
        self,
    ) -> dict[
        str, str | list[dict[str, dict[str, str | float | int] | int | float]] | float
    ]:
        return {
            "cart_id": self.cart_id,
            "items": [c.to_dict() for c in self.items],
            "total_price": self.total_price_cart(),
        }
