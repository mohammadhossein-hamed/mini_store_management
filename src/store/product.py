class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price if price > 0 else 0
        self.stock = stock if stock > 0 else 0

    def to_dict(self) -> dict[str, str | float | int]:
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data: dict[str, str | float | int]) -> "Product":
        return cls(
            name=str(data["name"]), price=float(data["price"]), stock=int(data["stock"])
        )

    def __str__(self) -> str:
        return f"{self.name.capitalize()} - ${self.price:.2f} (Stock: {"❌" if not self.stock else self.stock})"
