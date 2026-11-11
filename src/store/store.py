import os
from . import display
from .authentication import login, signup
from .cart import Cart
from .database import get_products, get_users, save_products, save_users
from .product import Product
from .user import User


class Store:
    cart = Cart()
    logged_as = ""

    def __init__(self) -> None:
        self.products: list[Product] = get_products()  # type: ignore
        self.users: list[User] = get_users()  # type: ignore

    # -------------------------------------Manging Menus----------------------------------- #

    def main_menu(self):
        """Displays main menu and navigates it based on the user's selection
        (1. View products, 2. Login/Signup/My Accoun, 3. Exit)"""
        return display.main_menu(self.logged_as)

    def admin_panel(self):

        while True:
            choice = display.admin_panel()
            match choice:
                case 1:
                    self.add_product()
                case 2:
                    self.delete_product()
                case 3:
                    self.admin_updata_product()
                case _:
                    break

    def customer_portal(self):
        """Displays customer portal and navigates it based on the user's selection
        (1.Add item to cart, 2.View cart, 3.Checkout, 4.Return to main menu)"""
        msg = ""
        while True:
            choice = display.customer_portal(
                [str(product) for product in self.list_products()], msg
            )
            match choice:
                case 1:
                    try:
                        product_num = int(input("Enter product number: "))
                        quantity = int(input("Enter quantity: "))
                        selected_product = self.list_products()[product_num - 1]
                        if 0 < quantity <= selected_product.stock:
                            self.add_to_cart(selected_product, quantity)
                            msg = f"\n ✅  Added {quantity} X {selected_product.name.capitalize()} to cart!\n"
                        elif quantity <= 0:
                            msg = "\n 📛  Quantity can't be less than one \n"
                        else:
                            msg = "\n 📛  More than product stock \n"
                    except Exception as e:
                        msg = f"❌ Error: {e}"

                case 2:
                    self.view_cart()
                    msg = ""
                case 3:
                    self.checkout()
                    msg = ""
                case _:
                    break

        os.system("clear")

    def user_panel(self):

        while True:
            choice = display.user_panel(str(self.logged_as))
            match choice:
                case 1:
                    self.view_cart()
                case 2:
                    self.checkout()
                case 3:
                    display.purchase_history(self.get_purchase_history())  # type: ignore
                    continue
                case _:
                    break

    def view_cart(self):
        """Displays the shopping cart and navigates it based on the user's selection
        (1.Back to shopping, 2.remove item from cart, 3.checkout)"""

        if not self.cart.items:
            os.system("clear")
            input(" 🛒  Your cart is empty")
        else:
            msg = ""
            while True:
                choice = display.cart(
                    msg,
                    [str(item) for item in self.cart.view_cart()],
                    self.cart.total_price_cart(),
                )
                match choice:
                    case 2:
                        try:
                            item_num = int(input("Enter product number to remove:"))
                            quantity = int(input("Enter quantity: "))
                            if 0 < quantity <= self.cart.items[item_num - 1].quantity:
                                msg = f"\n 🗑️  Removed {quantity} X {self.cart.items[item_num - 1].product.name.capitalize()} from cart.\n"
                                self.remove_from_cart((item_num - 1), quantity)
                            elif quantity <= 0:
                                msg = "\n 📛  Quantity can't be less than one \n"
                            else:
                                msg = "\n 📛  More than item quantity \n"
                        except Exception as e:
                            msg = f"\n❌ Error: {e}\n"
                    case 3:
                        if self.checkout():
                            break
                        else:
                            msg = ""
                    case _:
                        return
                if not self.cart.items:
                    break
                os.system("clear")

    # -------------------------------------- Managing Users ----------------------------- #

    def authentication(self):
        if self.logged_as:
            self.user_panel()
        else:
            msg = ""
            while True:
                choice = display.authentication(msg)
                match choice:
                    case 1:
                        self.logged_as, msg = login()
                    case 2:
                        self.logged_as, msg = signup()
                        self.users = get_users()  # type: ignore
                    case 3:
                        break
                    case _:
                        continue

                if self.logged_as == "admin":
                    self.admin_panel()
                    self.logged_as = ""
                    break
                elif self.logged_as:
                    break
                else:
                    continue

    def add_purchase_history(self):

        for user in self.users:
            if self.logged_as == user["username"]:  # type:ignore
                user["purchase_history"].append(self.cart.to_dict())  # type: ignore
                save_users(self.users)  # type: ignore

    def get_purchase_history(self) -> list[Cart] | None:

        for user in self.users:
            if self.logged_as == user["username"]:  # type: ignore
                return user["purchase_history"]  # type: ignore

        return None

    # -------------------------------------- Managing Products -------------------------- #

    def add_product(self):
        """Add new product to the store by the admin"""
        msg = ""
        while True:
            try:
                name, price, stock = display.add_product(msg=msg)
                if name.lower() == "done":
                    break

                if self.find_product(name):
                    msg = "\n ⛔️  A product with this name is already registered.\n"
                else:
                    if name != "" and price > 0 and stock > 0:
                        new_product = Product(name, price, stock)
                        self.products.append(new_product.to_dict())  # type: ignore
                        save_products(self.products)  # type: ignore
                        msg = f"\n✅ Product added: {new_product}\n"
                    else:
                        msg = "\n ⛔️  Price and Stock can't be less than one. \n"
            except Exception as e:
                msg = f"\n ❌  Error: {e}\n"

    def delete_product(self):
        msg = ""
        while True:
            choice = display.delete_product(
                [str(product) for product in self.list_products()], msg
            )

            if choice == "done":
                break

            try:
                product_num = int(choice) - 1
                if product_num < len(self.products):
                    msg = f"\n 🗑️  Deleted {self.products[product_num]["name"]} from Store !\n"  # type: ignore
                    del self.products[product_num]
                    save_products(self.products)  # type: ignore
                else:
                    msg = "\n ‼️  Wrong product number\n"
            except Exception as e:
                msg = f"\n❌ Error: {e}\n"

    def list_products(self) -> list[Product]:
        """Return list of products object"""
        return [Product.from_dict(product) for product in self.products]  # type: ignore

    def find_product(self, name: str):
        for product in self.products:
            if name.lower() == product["name"].lower():  # type: ignore
                return True

        return False

    def admin_updata_product(self):
        msg = ""
        while True:
            try:
                choice, new_stock, new_price = display.update_product(
                    [str(product) for product in self.list_products()], msg
                )

                if choice == "done":
                    break

                product_num = int(choice) - 1
                if product_num < len(self.products):
                    if new_stock >= 0 and new_price >= 1:
                        self.products[product_num]["stock"] = new_stock  # type: ignore
                        self.products[product_num]["price"] = new_price  # type: ignore
                        save_products(self.products)  # type: ignore
                        msg = f"\n ☑️  {self.products[product_num]["name"]} stock and price updated.\n"  # type: ignore
                    else:
                        msg = (
                            "\n ⛔️  Product stock and price cannot be less than zero. "
                        )
                else:
                    msg = "\n ‼️  Wrong product number\n"
            except Exception as e:
                msg = f"\n❌ Error: {e}\n"

    def update_product(self, product: Product, quantity: int = 0, price: float = 0):
        """Update product stock after adding or removing from cart"""
        for item in self.products:
            if item["name"] == product.name:  # type: ignore
                if quantity:
                    item["stock"] += quantity  # type: ignore
                if price:
                    item["price"] == price  # type: ignore
                break
        save_products(self.products)  # type: ignore

    # ------------------------------------ Managing Cart --------------------------------------- #

    def add_to_cart(self, product: Product, quantity: int = 1):
        self.cart.add_to_cart(product, quantity)
        self.update_product(
            product,
            -quantity,
        )

    def remove_from_cart(self, item_num: int, quantity: int):
        self.update_product(
            self.cart.items[item_num].product,
            +quantity,
        )
        self.cart.remove_from_cart(item_num, quantity)

    def delete_cart(self):
        if not self.cart.items:
            return
        else:
            for item in self.cart.items:
                self.update_product(
                    item.product,
                    +item.quantity,
                )

            return

    def checkout(self) -> bool:

        if not self.cart.items:
            os.system("clear")
            input(
                """
                \r ❗️ You have not added any items to your cart yet."""
            )

        elif self.cart.items and self.logged_as:
            choice = display.checkout(
                [str(item) for item in self.cart.view_cart()],
                self.cart.total_price_cart(),
                True,
            )
            match choice:
                case 1:
                    self.add_purchase_history()
                    self.cart = Cart()
                    input("\n 🎉  Thank you for shopping with us! \n")
                    return True
                case _:
                    return False
        else:
            display.checkout(
                [str(item) for item in self.cart.view_cart()],
                self.cart.total_price_cart(),
                False,
            )
        return False
