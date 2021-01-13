class Emp:
    # Class Variable:
    no_of_leaves = 8
    pass


Mayur = Emp()
Soniya = Emp()

# Instance Variable
Mayur.name = "Mayu"
Mayur.salary = 45000
Mayur.age = 23

Soniya.name = "soni"
Soniya.salary = 13000
Soniya.age = 23

print(Mayur.name, Soniya.salary)
print(Soniya.no_of_leaves)
print(Emp.__dict__)
no_of_leaves = 10
print(Mayur.__dict__)
print(Soniya.__dict__)
print(Emp.no_of_leaves)
