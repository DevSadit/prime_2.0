# Design and create an online store for products (name, price).
#  track total products being created.
#  Create a static method to calculate discount on each product based on a % parameter.


class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"product name : {self.name} and product price: {self.price}")

    @classmethod
    def get_count(cls):
        print(f"{Product.count} product created")

    @staticmethod
    def calc_discoint(price, discount):
        print(f"discounted price: {price - (price*discount / 100)}")


p1 = Product("kola", 6)
p3 = Product("alo", 50)
p1.get_info()

# check how many products are there.
Product.get_count()


p3.calc_discoint(p3.price, 10)
