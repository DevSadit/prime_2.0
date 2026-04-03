# there are 3 types of method.
# 1. isinstance
# 2. class
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


l1 = Laptop(16, 256)
l2 = Laptop(32, 512)


l1.get_info()
