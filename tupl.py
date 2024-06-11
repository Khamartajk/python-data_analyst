# tupl1=("apple","cherry","grapes","apple")
# tupl2=(12,)
# print (type(tupl2))

# print(tupl1)
# print(tupl1[0])

# Dictionaries

student_info={
    "Rollno":"102",    
    "Name":"suresh",
    "Marks" :"98%",
    "city":"Hyderabad",
    "phone":"567643487"
}

# print (deepak_info)
# print(len(deepak_info))

thisdict=dict(name="john", age =36,country="Norway")
# print(thisdict)

fname = student_info["Name"]
rollno=student_info["Rollno"]
# print(fname)
# print(rollno)


student_info["email"]="asd@vfg.com"
x = student_info.keys()
y = student_info.values()

# print (x)
# print(y)


car={
    "brand":"Ford",
    "model": "mustang",
    "year" :1977
}

# if "color" in car:
#     print("Yes,'model' is one of the keys in this dictionaries")
# else:
#     print("No,it is not there in this dictionary")

car.update({"year":"2020"})

# print(car)


# student_info.pop("email")
# del student_info["Rollno"]
# print(student_info)

# car.clear()
# print(car)

for x,y in student_info.items():
    print(x, ':',y)

mycar = car.copy()
print(mycar)