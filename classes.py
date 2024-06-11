class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def myfunc(self):
        print("Hello my name is "+ self.name)

obj1 = person("john",34)
print(obj1.age)
print(obj1.name)
obj1.age = 40
print(obj1.age)
print(obj1.myfunc())

del obj1.age
print(obj1.myfunc())



class student:
    pass