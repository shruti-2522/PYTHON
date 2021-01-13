# Class Method:
class Emp:
    no_of_leaves = 7

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def printdetails(self):
        return f"name is:{self.name} salary is{self.salary} and age is{self.age}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


Shruti = Emp('shruti', 43000, 22)
# print(Shruti.printdetails())
Shruti.change_leaves(45)
print(Shruti.no_of_leaves)
