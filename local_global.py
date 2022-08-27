y=2
def a():
   y=2
   x=2
   return(x+y)
print(a())



n=4
def sum():
   global a
   a=3
   print(a+n)
sum()


def a():
   x=3
   def b():
      y=13
      print(x,y)
   b()
   print(x)
a()


def a():
   print(9+1)
def b():
   print("Reena")
def fun():
   x=10
   b()
   a()
   print(x)
fun()


