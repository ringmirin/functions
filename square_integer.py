# Create a function which takes one argument (a positive integer) and returns a dictionary which has 
# numbers from 1 to the integer (passed as parameter) as the keys and their respective squares as the 
# values as shown in the example below



def sqr():
   b=dict()
   for i in range(1,20):
      b[i]=i**2
   return b
# c=sqr()
print(sqr())