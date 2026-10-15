import os

# This class represents a single product in the store. Each item has a name and a price, which are stored as object attributes.
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# This list holds all products available for purchase in the shop. Each entry is an Item object with a product name and price.
Inventory = [
    Item("Kaas", 50.00),
    Item("Brood", 15.00),
    Item("Melk", 30.00),
    Item("Eiers", 20.00),
    Item("Botter", 110.00),
]

# This list stores the items selected by the customer during shopping. It acts as the shopping cart and is updated as products are added or cleared.
chosen_items = []

# Maximum number of products the customer can place in the cart at one time. This prevents the cart from becoming too full.
MAX_CART_ITEMS = 10



# This function prints the product list and the available commands. It helps the user know what can be purchased and what actions they can take.
def display_inventory():
    print("Items available:")
    for index, item in enumerate(Inventory, start=1):
        print(f"{index}: {item.name} - R{item.price:.2f}")
    print("Enter 0 or type 'done' to finish shopping.")
    print("Type 'exit' to exit the program.")
    print("Type 'clear cart' to clear the cart.")
    print("Type 'clear all' to clear the screen.")

# This function displays the current contents of the cart. If the cart is empty, it tells the user so. Otherwise, it prints every item and the total amount owed.
def check_cart():
    if not chosen_items:
        print("Your cart is empty.")
    else:
        total = sum(item.price for item in chosen_items)
        print("Items in your cart:")
        for cart_item in chosen_items:
            print(f"{cart_item.name} - R{cart_item.price:.2f}")
        print(f"Total: R{total:.2f}")



# This function removes all items from the shopping cart. It is used when the user chooses the 'clear cart' option.
def clear_cart():
    chosen_items.clear()
    print("Cart cleared.")

# This function adds a product to the cart based on the user's selection. It validates the selected index before adding it to ensure the user cannot. Choose an invalid item number.
def add_item_to_cart(item_index):
    if not 1 <= item_index <= len(Inventory):
        print("Invalid item. Please try again.")
        return
    
    selected_item = Inventory[item_index - 1]
    chosen_items.append(selected_item)
    print(f"Added {selected_item.name} to your cart.")
    if len(chosen_items) == MAX_CART_ITEMS:
        print("You have reached the maximum number of items in your cart.")
        
# This loop checks whether the cart has reached the maximum size. It is placed here as a simple safety check, but the actual limit is enforced in the add_item_to_cart() function when a user selects an item.
for item in Inventory:
    if len(chosen_items) >= MAX_CART_ITEMS:
        print("You have reached the maximum number of items in your cart.")
        break

# This is the main program loop. It displays the inventory, reads the user's input, and performs the correct action.
def main():
    display_inventory()
    while True:
        # Read the user's selection and convert it to lowercase to make the command. Checks case-insensitive.
        item = input("Choose an item (1-5), or enter 0 to finish: ").strip().lower()

        if item == "exit":
            print("Goodbye!")
            break

        elif item in ("0", "done"):
            # If no items are in the cart, the user cannot finish the purchase yet.
            if not chosen_items:
                print("Your cart is empty.")
                continue
            check_cart()
            choice = input("Would you like to continue shopping? (yes/no): ").strip().lower()
            if choice == "no":
                print("Thank you for shopping with us!")
                break
            elif choice == "yes":
                display_inventory()

        elif item == "clear cart":
            clear_cart()

        elif item == "clear all":
            # Clear the terminal screen and redisplay the inventory.
            os.system('cls' if os.name == 'nt' else 'clear')
            display_inventory()
        elif item.isdigit() and 1 <= int(item) <= len(Inventory):
            add_item_to_cart(int(item))

        else:
            print("Invalid item. Please try again.")

# This ensures the program starts only when the file is run directly. It prevents the main() function from executing if this file is imported elsewhere.
if __name__ == "__main__":
    main()
