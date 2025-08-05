import random

# Product Class
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (₹{self.price})"

# User Class
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

# Cart Class
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append({'product': product, 'quantity': quantity})

    def get_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items)

    def show_cart(self):
        print("\n🛒 Cart Summary:")
        for item in self.items:
            print(f"- {item['product']} x {item['quantity']}")

# Order Class
class Order:
    def __init__(self, user, cart):
        self.order_id = random.randint(1000, 9999)
        self.user = user
        self.cart = cart
        self.total = cart.get_total()

    def summary(self):
        print("\n🧾 Order Summary")
        print(f"Order ID   : {self.order_id}")
        print(f"Customer   : {self.user.name}")
        self.cart.show_cart()
        print(f"\nTotal Bill : ₹{self.total}")

# -------- Main Program --------
if __name__ == "__main__":
    # Sample Data
    user1 = User(1, "Rohan")
    product1 = Product(101, "Laptop", 50000)
    product2 = Product(102, "Mouse", 500)
    product3 = Product(103, "Keyboard", 1000)

    # Cart Process
    cart = Cart()
    cart.add_product(product1, 1)
    cart.add_product(product2, 2)
    cart.add_product(product3, 1)

    # Order Process
    order = Order(user1, cart)
    order.summary()
