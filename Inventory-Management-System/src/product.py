class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"{self.product_id} | {self.name} | Rs.{self.price} | Qty: {self.quantity}"



