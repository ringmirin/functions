##write a python program to get all the factorial of non negative integer

def recursion(n):
   if n<=1:
      return n
   else:
      return n*(recursion(n-1))
print(recursion(5))


