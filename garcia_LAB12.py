def display_menu():
    menu = {
        1: ("Spaghetti", 45.00),
        2: ("Palabok", 25.00),
        3: ("Carbonara", 45.00),
        4: ("Fried Chicken", 20.00),
        5: ("Barbeque", 15.50)

    }
    print("\nMenu:")
    for item, details in menu.items():
        print(f"{item}. {details[0]} - ₱{details[1]:.2f}")
    return menu

def take_order(menu):
    while True:
        try:
            choice = int(input("\nEnter the number of the item you want to order: "))
            if choice in menu:
                item_name, item_price = menu[choice]
                print(f"You selected: {item_name} (₱{item_price:.2f})")
                return item_price
            else:
                print("Invalid choice. Please select an item from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def process_payment(total_cost):
    while True:
        try:
            cash = float(input(f"\nTotal cost is ₱{total_cost:.2f}. Enter cash amount: "))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment successful! Your change is ₱{change:.2f}.")
                break
            else:
                print(f"Insufficient cash. You need at least ₱{total_cost - cash:.2f} more.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    print("Welcome to the Food Ordering System!")
    menu = display_menu()
    total_cost = take_order(menu)
    process_payment(total_cost)
    print("\nThank you for your order! Enjoy your meal!")

if __name__ == "_main_":
    main()
