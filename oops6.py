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

    # class method can called as alternative constructor:
    @classmethod
    def from_str(cls, String):
        # param = String.split('-')
        # print(param)
        # return cls(param[0], param[1], param[2])
        return cls(*(String.split("-")))

    @staticmethod
    def msg(String):
        print("hello" + String)
        return 1


Shruti = Emp('shruti', 43000, 22)
Shubh = Emp.from_str("Shubham-70000-25")
print(Shubh.salary)
print(Shubh.msg("Shruti"))

# print(Shruti.printdetails())
Shruti.change_leaves(45)
print(Shruti.no_of_leaves)
