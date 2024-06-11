# def calc_sum(a,b):
#     sum = a+ b
#     return(sum)

# result = calc_sum(25,35)
# print("return value is : ",result)

# print("welcome",end="")
# print("learn python")
# print(len("welcome"))
# print(type("welcome"))

#WAF to print the length of list(list is the parameter)

cities=["Mumbai","Delhi","Chennai","Bangalore","Hyderabad","Kolkatta","Pune"]
heroes=["Shaktiman","Power Rangers","BatMan","SpiderMan","SuperMan"]

# def print_len(list):
#     print(len(list))
#     return(len(list))

# print_len(heroes)

# print(len(cities))


#WAF to print the elements pf a list in a single line (list is the parameter)

# def print_list(list):
#     for item in list:
#         print(item)

# print_list(heroes)

#WAF to find factorial of a number(n is the given number)

#n=5, 5*4*3*2*1

# def calc_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)


# calc_fact(6)  

#Home work: WAF to conert usd into INR


def usd_converter(usd):
    inr = 83
    inr = inr * usd
    print(usd ," dollars =",inr,"INR")
    return (inr)

Inr = usd_converter(500)
print(Inr)

