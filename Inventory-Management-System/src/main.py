

from inventory import Inventory
from product import Product

inventory = Inventory()

def show_menu():
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        qty = int(input("Enter Quantity: "))

        product = Product(pid, name, price, qty)
        inventory.add_product(product)
        print("Product added successfully!")

    elif choice == "2":
        inventory.view_products()

    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Try again.")
