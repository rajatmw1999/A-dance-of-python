
# var = 2
# print(type(var))

# print(var.bit_length())

# ------------

class Student():
    school = "MSIT"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def changeSchool(cls):
        cls.school = "SVMSSS"
    # pass

s1 = Student("Rajat",22)
s2 = Student(60,"Bill")

print(Student.school)
Student.changeSchool()
print(Student.school)
# print(s1.name,s1.age)
# print(s2.name,s2.age)
