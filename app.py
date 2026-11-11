from src import Store

store = Store()


def app():
    """Run the app."""
    global is_logged_in, logged_as
    app_running = True
    while app_running:
        choice = store.main_menu()
        match choice:
            case 1:
                store.customer_portal()

            case 2:
                store.authentication()
            case _:
                store.delete_cart()
                app_running = False
                print("\nClosing App. Goodbye!\n")


def main():
    app()


if __name__ == "__main__":
    main()
