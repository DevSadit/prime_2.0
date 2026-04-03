# attribute
# 1. class
# 2. isinstance


# the things which are common they comes under class attribute.
# ex:
# university, country, --> class attribute

# the things which could be different they comes under instances.
# ex:
# name, id, roll, age --> isinstance


class Student:

    #  class attribute
    uni_name = "PUC"

    # instances
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


s1 = Student("samiya", 20, "02225923409")


print(s1.name, s1.age, s1.id)

# accesing the class attribute
print(Student.uni_name)
print(s1.uni_name)
