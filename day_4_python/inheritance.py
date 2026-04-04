# Inheritance --> reusing attribute and methods from a parent(base) class.


class Person:
    resident = "Bangladeshi"
    city = "chittagong"

    def print_name(self):
        print(self.fname, self.lname)


# p1 = Person("ahmed", "shah")
# p1.print_name()


class Student(Person):
    def __init__(self, subject):
        self.subject = subject

    def change_city(self, new_city):
        city = new_city

    def get_all_info(self):
        print(self.subject)
        print(self.city)
        print(self.resident)


s1 = Student("Programming")

s1.get_all_info()
