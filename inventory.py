
inventory = []
def display_menu():
    print("========== Inventory Management System ==========")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Search and Retrieve Product")
    print("5. Display Inventory")
    print("6. Exit")
    print("===============================================")

def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-6): ")
        if choice.isdigit() and 1 <= int(choice) <= 6:
            return int(choice)
        print("Invalid choice. Please enter a valid option.")

def add_product():
    print("========== Add Product ==========")
    # Prompt the user to enter product details

    product_name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))

    # Add the product to the inventory
    # Your implementation here
    product = {
        "name": product_name,
        "id": product_id,
        "price": product_price,
        "quantity": product_quantity
    }

    inventory.append(product)


    print("Product added successfully!")

def update_product():
    print("========== Update Product ==========")
    # Prompt the user to enter the product ID to update
    product_id = input("Enter product ID to update: ")
    product = None
    for p in inventory:
        if p["id"] == product_id:
            product = p
            break
    if product is None:
        print("Product not found")
        return

    updated_name = input(f"Enter updated name for product {product_id}: ")
    updated_price = input(f"Enter updated price for product {product_id}")
    updated_quantity = input(f"Enter updated quantity for product {product_id}")

    product["name"] = updated_name
    product["price"] = updated_price
    product["quantity"] = updated_quantity

    print("Product updated successfully!")

def delete_product():
    print("========== Delete Product ==========")
    # Prompt the user to enter the product ID to delete
    product_id = input("Enter product ID to delete: ")

    product = None
    for p in inventory:
        if p["id"] == product_id:
            product = p
            break

    if product is None:
        print("Product not found.")
        return

    inventory.remove(product)

    print("Product deleted successfully!")

def search_product():
    print("========== Search and Retrieve Product ==========")
    # Prompt the user to enter search criteria (e.g., name, ID, price range)
    search_criteria = input("Enter search criteria: ")
    matching_products = []

    for product in inventory:
        if search_criteria.lower().strip()==product["name"].lower():
            matching_products.append(product)

    if not matching_products:
        print("No matching products found.")
        return

    print(f"Found {len(matching_products)} matching product(s): ")
    for product in matching_products:
        print("----------")
        print(f"Name: {product['name']}")
        print(f"ID: {product['id']}")


def display_inventory():
    print("========== Inventory ==========")
    # Display the inventory
    # Your implementation here
    for index,product in enumerate(inventory):
        print(f"{index+1}.:{product['name']}")
        print(f"ID: {product['id']}")
        print(f"Price: {product['price']}")
        print(f"Quantity: {product['quantity']}")
        print()

# Main program
while True:
    display_menu()
    choice = get_menu_choice()

    if choice == 1:
        add_product()
    elif choice == 2:
        update_product()
    elif choice == 3:
        delete_product()
    elif choice == 4:
        search_product()
    elif choice == 5:
        display_inventory()
    else:
        print("Thank you for using the Inventory Management System. Goodbye!")
        break
