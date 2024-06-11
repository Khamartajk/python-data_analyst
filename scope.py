# x = 400
# def myfunc():
#   x = 300
#   print(x)

# myfunc()
# print(x)

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()