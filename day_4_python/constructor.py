# creating a class
class Student:
    # constructor created
    def __init__(self, name, cgpa):
        print("constructor called & new object created")
        self.name = name
        self.cgpa = cgpa


# creating object
s1 = Student("sadit", 3.9)
s2 = Student("rakib", 2.7)

print(s2.name)
print(s2.cgpa)
