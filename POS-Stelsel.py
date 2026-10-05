import os

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

Inventory = [
    Item("Kaas", 50.00),
    Item("Brood", 15.00),
    Item("Melk", 30.00),
    Item("Eiers", 20.00),
    Item("Botter", 110.00),
]
chosen_items = []
MAX_CART_ITEMS = 10

for item in Inventory:
    if len(chosen_items) >= MAX_CART_ITEMS:
        print("You have reached the maximum number of items in your cart.")
        break

def display_inventory():
    print("Items available:")
    for index, item in enumerate(Inventory, start=1):
        print(f"{index}: {item.name} - R{item.price:.2f}")
    print("Enter 0 or type 'done' to finish shopping.")
    print("Type 'exit' to exit the program.")
    print("Type 'clear cart' to clear the cart.")
    print("Type 'clear all' to clear the screen.")

def check_cart():
    if not chosen_items:
        print("Your cart is empty.")
    else:
        total = sum(item.price for item in chosen_items)
        print("Items in your cart:")
        for cart_item in chosen_items:
            print(f"{cart_item.name} - R{cart_item.price:.2f}")
        print(f"Total: R{total:.2f}")

def clear_cart():
    chosen_items.clear()
    print("Cart cleared.")

def add_item_to_cart(item_index):
    if not 1 <= item_index <= len(Inventory):
        print("Invalid item. Please try again.")
        return

    selected_item = Inventory[item_index - 1]
    chosen_items.append(selected_item)
    print(f"Added {selected_item.name} to your cart.")
    if len(chosen_items) == MAX_CART_ITEMS:
        print("You have reached the maximum number of items in your cart.")


  
def main():
    
    display_inventory()
    while True:
        item = input("Choose an item (1-5), or enter 0 to finish: ").strip().lower()

        if item == "exit":
            print("Goodbye!")
            break

        elif item in ("0", "done"):
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
            os.system("cls")
            display_inventory()
        elif item.isdigit() and 1 <= int(item) <= len(Inventory):
            add_item_to_cart(int(item))

        else:
            print("Invalid item. Please try again.")

if __name__ == "__main__":
    main()
