from store.product import Product


class CartItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def __str__(self) -> str:
        return f" - {self.product.name.capitalize()} X {self.quantity} - ${self.total_price_item():.2f}"

    def total_price_item(self) -> float:
        return self.quantity * self.product.price

    def to_dict(self) -> dict[str, dict[str, str | float | int] | int | float]:
        return {
            "product": self.product.to_dict(),
            "quantity": self.quantity,
            "total_price": self.total_price_item(),
        }
