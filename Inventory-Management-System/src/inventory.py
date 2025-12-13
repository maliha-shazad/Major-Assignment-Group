from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def view_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\nID | Name | Price | Quantity")
        for product in self.products:
            print(product.display())


