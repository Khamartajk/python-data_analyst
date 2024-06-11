# program to check even or odd number

# num1=int(input("Enter the number"))
# if (num1 % 2)==0:
#     print("even number")
# else:
#     print("odd number")

indian=["samosa","daal","naan","vada"]
chinese=["noodles","fried-rice","egg role","momos"]
italian=["pizza","pasta","risotto"]

dish = input("enter the dish name")

if dish in indian:
    print("Indian Cuisine")
elif dish in chinese:
    print("chinese Cuisine")
elif dish in italian:
    print("Italian Cuisine")
else:
    print("According to me i do not know this",dish)
    