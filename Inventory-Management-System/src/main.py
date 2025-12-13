from inventory import Inventory
from product import Product

inventory = Inventory()

def show_menu():
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Exit")

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
        pid = input("Enter Product ID to search: ")
        product = inventory.search_product(pid)
        if product:
            print("Product Found:")
            print(product.display())
        else:
            print("Product not found.")

    elif choice == "4":
        pid = input("Enter Product ID to delete: ")
        if inventory.delete_product(pid):
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Try again.")
