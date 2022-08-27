# Write a Python program to find  the greatest common divisor (gcd) of two 
# integers

def recursion_gcd(x,y):
   if (y==0):
      return x
   else:
      return recursion_gcd(y,x%y)
a=48
b=60
print(recursion_gcd(a,b)) 


