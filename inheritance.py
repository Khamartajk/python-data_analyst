class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

# stud1 = Person("Santosh","Infant")
# stud1.printname()


class student(Person):
   def __init__(self,fname,lname):
       super.__init__(self,fname,lname)



obj1 = student("Khamartaj","Kalegar")
obj1.printname()