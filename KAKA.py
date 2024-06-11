# Party Hire Phone Order System

menu = {
    1: {"name": "Bouncy Castle", "price": 5},
    2: {"name": "Balloon Kit", "price": 5},
    3: {"name": "Party Hats", "price": 5},
    4: {"name": "Tables", "price": 7},
    5: {"name": "Chairs", "price": 7},
    6: {"name": "Banners", "price": 7}
}

def get_customer_info(order_type):
    if order_type == "D":
        customer_name = input("Enter customer's name: ")
        address = input("Enter delivery address: ")
        phone_number = input("Enter phone number: ")
        delivery_charge = 3
    else:
        customer_name = input("Enter customer's name: ")
        delivery_charge = 0
        address, phone_number = None, None  # Not needed for pickup orders
    return customer_name, address, phone_number, delivery_charge

def display_menu():
    print("\nMenu:")
    for item_num, item in menu.items():
        print(f"{item_num}. {item['name']} (${item['price']:.2f}")

def calculate_order_cost(ordered_items, delivery_charge):
    total_cost = sum(menu[item_num]['price'] for item_num in ordered_items)
    total_cost += delivery_charge
    return total_cost

def display_order_details(customer_name, ordered_items, total_cost, address=None, phone_number=None):
    print("\nOrder Details:")
    print(f"Customer Name: {customer_name}")
    print(f"Ordered Items: {', '.join(menu[item_num]['name'] for item_num in ordered_items)}")
    print(f"Total Cost: ${total_cost:.2f}")
    if address and phone_number:
        print(f"Delivery Address: {address}")
        print(f"Phone Number: {phone_number}")

def main():
    print("Welcome to Party Hire Phone Order System!")
    order_type = input("Is the order for pickup or delivery? (P/D): ").upper()

    customer_name, address, phone_number, delivery_charge = get_customer_info(order_type)

    display_menu()

    num_items = int(input("How many items would you like to order (max 3)? "))
    if num_items > 3:
        print("Maximum 3 items allowed per order.")
        return

    ordered_items = []
    for _ in range(num_items):
        item_num = int(input("Enter item number (1-6): "))
        if item_num not in menu:
            print("Invalid item number. Please choose from the menu.")
            return
        ordered_items.append(item_num)

    total_cost = calculate_order_cost(ordered_items, delivery_charge)

    display_order_details(customer_name, ordered_items, total_cost, address, phone_number)

if __name__ == "__main__":
    main()
