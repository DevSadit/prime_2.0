# there are 3 types of method.
# 1. isinstance -> where the first parameter is - self
# 2. class -> where the first parameter is - cls
# 3. static


class Laptop:
    storage_type = "ssd"

    # constructor
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    # making instance
    def get_info(self):
        print(f"Laptop RAM: {self.ram}")
        print(f"Laptop STORAGE: {self.storage}")

    # making class method
    @classmethod  # --> decorator
    def get_storage(cls):
        print(f"laptop storage: {cls.storage_type}")


l1 = Laptop(16, 256)
l2 = Laptop(32, 512)


l1.get_info()

# calling the class method
l2.get_storage()
Laptop.get_storage()
