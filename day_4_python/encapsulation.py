# ther are 4 pillars of oop.
# 1. encapsulation -> wrapping data & function into single unit.
# 2. abstraction
# 3. inheritance
# 4. polymorphism


# data hiding
# 1. public -> class inside and outside
# 2. protected -> class + subclass ==> : can be accesible from the outside of the class. but we should not. its a rule.
# 3. private -> inside the class: cant be accesible from the outside of the class. if we use, we will get error.


# To get the private attribute data outside the class, we use getter and setter function.


class BankAccoutn:
    def __init__(self, id, name, balance):
        self.id = id  # public attribute
        self._name = name  # protected attribute
        self.__balance = balance  # private attribute

    # setter function
    def set_bal(self, new_balance):
        self.__balance = new_balance

    # getter function
    def get_bal(self):
        return self.__balance


acc1 = BankAccoutn("0613412", "Rafique", 10000)

print(acc1.id, acc1._name)
acc1.set_bal(20_000)
print(acc1.get_bal(), "tk")


# another way to acces the private attribute
# print(acc1._BankAccoutn__balance)
