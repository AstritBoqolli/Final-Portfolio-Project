class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description=""):
        # Constructor for ItemToPurchase class
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        # Print the cost of the item
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


def main():
    # Prompt user for two items and create objects of the ItemToPurchase class
    items = []
    for i in range(2):
        print(f"Item {i + 1}")
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_description = input("Enter the item description:\n")
        item.item_price = float(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        items.append(item)

    # Output the costs of the two items
    print("\nTOTAL COST")
    for item in items:
        item.print_item_cost()

    # Calculate and output the total cost
    total_cost = sum(item.item_price * item.item_quantity for item in items)
    print(f"Total: ${total_cost}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # List to store items in the shopping cart

    def add_item(self, item):
        # Add an item to the shopping cart
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # Remove an item from the shopping cart by item name
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        # Modify an item in the shopping cart based on a modified_item
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                if modified_item.item_name != "none":
                    item.item_name = modified_item.item_name
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Get the total quantity of items in the shopping cart
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        # Get the total cost of items in the shopping cart
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        # Print the total and details of items in the shopping cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            item.print_item_cost()
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost}")

    def print_descriptions(self):
        # Print descriptions of items in the shopping cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu():
    # Print the main menu options
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    choice = input("Choose an option: ")
    return choice


def shopping_cart_main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date)

    while True:
        choice = print_menu()

        # Adding an item to the cart
        if choice == 'a':
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_description = input("Enter the item description:\n")
            item.item_price = float(input("Enter the item price:\n"))
            item.item_quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(item)

        # Removing an item from the cart
        elif choice == 'r':
            item_name = input("Enter the item name to remove:\n")
            cart.remove_item(item_name)

        # Modifying an item in the cart
        elif choice == 'c':
            modified_item = ItemToPurchase()
            modified_item.item_name = input("Enter the item name to modify:\n")
            modified_item.item_price = float(input("Enter the new item price (or 0 to keep it unchanged):\n"))
            modified_item.item_quantity = int(input("Enter the new item quantity (or 0 to keep it unchanged):\n"))
            modified_item.item_description = input("Enter the new item description (or press Enter to keep it unchanged):\n")
            cart.modify_item(modified_item)

        # Printing item descriptions
        elif choice == 'i':
            cart.print_descriptions()

        # Printing the total shopping cart
        elif choice == 'o':
            cart.print_total()

        elif choice == 'q':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
    shopping_cart_main()
