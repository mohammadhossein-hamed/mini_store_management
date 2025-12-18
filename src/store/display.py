import os


def main_menu(is_logged_in: str | bool) -> int:
    """Main menu"""
    os.system("clear")

    while True:
        choice = input(
            f"""=================================
            \r         🛍️  MINI STORE 
            \r=================================
            \r
            \r  👋 Welcome!
            
            \r1. View Products
            \r2. {"My Account" if is_logged_in else "Login/Signup"}
            \r3. Exit App
            
            \rEnter choice: """
        )
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            input(
                """
                \rPlease choose one of the options above.
                \rPress enter to try again."""
            )

            os.system("clear")


# ------------------------------------- Customer Portal ------------------------------------------- #


def customer_portal(list_products: list[str], msg: str = ""):
    """Customer portal"""
    os.system("clear")
    while True:
        print(msg)
        print(
            f"""=================================
            \r      🛍️  CUSTOMER PORTAL
            \r=================================
            \r
            \rAvailable products:\n"""
        )
        for index, product in enumerate(list_products):
            print(f"[{index+1}] {str(product)}")

        choice = input(
            """
            \r--------------------
            \r1. Add item to cart
            \r2. View cart
            \r3. Checkout
            \r4. Return to main menu
            \r--------------------
            \rEnter choice: """
        )

        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        else:
            input(
                """
                \rPlease choose one of the options above.
                \rPress enter to try again."""
            )

            os.system("clear")


# ----------------------------------------- Authentication panel -------------------------------- #


def authentication(msg: str):
    """Authentication panel"""
    os.system("clear")
    while True:
        print(msg)
        choice = input(
            """=================================
            \r      🔐  Store User Login
            \r=================================\n
            \r1. Login
            \r2. Signup
            \r3. Return to Main menu
            \rEnter choice: """
        )
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            input(
                """
                \rPlease choose one of the options above.
                \rPress enter to try again."""
            )


# ------------------------------------------- User panels -------------------------------------- #


def user_panel(username: str):
    """Main user panel"""
    os.system("clear")
    while True:
        choice = input(
            f"""=================================
            \r      👤  {username.capitalize()}
            \r=================================\n
            \r1. View cart
            \r2. Checkout
            \r3. Purchase history
            \r4. Return to main menu
            \rEnter choice: """
        )

        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        else:
            input(
                """
                \rPlease choose one of the options above.
                \rPress enter to try again."""
            )


def cart(msg: str, cart_items: list[str], total: float):
    """Cart view"""
    os.system("clear")
    print(msg)
    print(
        f"""=================================
        \r        🛒  Your cart:
        \r================================= \n"""
    )
    for index, item in enumerate(cart_items):
        print(f"[{index+1}] {str(item)}")
    print(f"\n 💰 Total: ${total:.2f}")
    choice = input(
        """
        \r--------------------
        \r1. Back to shopping
        \r2. Remove item from cart
        \r3. Checkout
        \r--------------------
        \rEnter choice: """
    )

    if choice in ["1", "2", "3"]:
        return int(choice)
    else:
        input(
            """
            \rPlease choose one of the options above.
            \rPress enter to try again."""
        )


def checkout(cart_items: list[str], total: float, is_logged_in: bool):
    """Checkout view"""
    os.system("clear")
    print(
        f"""🧾 Final Checkout:  
                  
        \r{"\n".join(cart_items)}

        \r💳 Total amount due: ${total:.2f}
  """
    )
    if is_logged_in:
        choice = input(
            """
                \r--------------------
                \r1. Approve
                \r2. Cancel
                \r--------------------
                \rEnter choice: """
        )

        if choice in ["1", "2"]:
            return int(choice)
        else:
            input(
                """
                \rPlease choose one of the options above.
                \rPress enter to try again."""
            )
    else:
        input(
            """
            \r--------------------
            \rYou must Login first
            \r--------------------
            """
        )


def purchase_history(history):  # type: ignore
    """Purchase history view"""
    os.system("clear")

    if not history:
        input("❌ There is no purchase history for You.")

    else:
        print(
            f"""\n  🗓️  Your purchase history
              \r********************************\n"""
        )
        for index, cart in enumerate(history):  # type: ignore
            print(f"\n🛒 Shopping #{index+1} \n")
            for item in cart["items"]:  # type: ignore
                print(
                    f" - {(item["product"]["name"]).capitalize()} X {item["quantity"]} - ${item["total_price"]:.2f}"  # type: ignore
                )
            print(f"\n 💳️  Total amount: ${cart["total_price"]:.2f}")
        print("\n\n********************************\n")
        input("Press Enter to Back.")


# -------------------------------------------- Admin panels ------------------------------------- #
def admin_panel():
    """Main admin panel"""
    os.system("clear")
    while True:
        choice = input(
            f"""=================================
            \r         💼  Admin Panel
            \r=================================\n
            \r1. Adding new produc
            \r2. Deleting product
            \r3. Updating product stock and prices
            \r4. Exit
            \rEnter choice: """
        )

        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        else:
            input(
                """
                \rPlease choose one of the options above.
                \rPress enter to try again."""
            )


def add_product(msg: str = ""):
    """Add product by admin view"""
    os.system("clear")
    print(msg)
    print(
        """=================================
        \r       📦  Adding Products
        \r=================================\n"""
    )

    name = str(input("Enter product name (or 'done' to finish): "))
    if name.lower() != "done":
        price = float(input("Enter product price:"))
        stock = int(input("Enter product stock quantity:"))
        return name, price, stock

    return "done", 0, 0


def delete_product(list_products: list[str], msg: str = ""):
    """Delete product by admin view"""
    os.system("clear")
    print(msg)
    print(
        """=================================
        \r       ⚰️  Deleting Product
        \r=================================\n
        \rAll Products: """
    )
    for index, product in enumerate(list_products):
        print(f"[{index+1}] {str(product)}")
    product_num = input("\nEnter product number (or 'done' to finish):")

    return product_num


def update_product(list_products: list[str], msg: str = ""):
    """Update product panel view"""
    os.system("clear")
    print(msg)
    print(
        """=================================
        \r       🔄  Updating Product
        \r=================================\n
        \rAll Products: """
    )
    for index, product in enumerate(list_products):
        print(f"[{index+1}] {str(product)}")

    product_num = input("\nEnter product number You want update (or 'done' to finish):")
    if product_num.lower() != "done":
        new_stock = int(input("Enter the new product stock: "))
        new_price = float(input("Enter the new product price: "))
        return product_num, new_stock, new_price

    return "done", 0, 0
