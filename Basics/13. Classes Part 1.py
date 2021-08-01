class Student:
    uniform = True

    def __init__(self, name, standard):
        self.name = name
        self.standard = standard
    
    def showStudent(self):
        print("Name: " + self.name + "\nStandard: " + self.standard)
        return "Got it"


goutham = Student("Goutham","12")


# goutham.uniform = False
# print(goutham.uniform)

# print(goutham.showStudent())


print(hasattr(goutham, 'name'))

# The getattr(obj, name[, default]) − to access the attribute of object.

# The hasattr(obj,name) − to check if an attribute exists or not.

# The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

# The delattr(obj, name) − to delete an attribute.