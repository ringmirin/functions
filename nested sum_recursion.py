# Write a Python program of recursion list sum.

# test=[1, 2, [3,4], [5,6]]



def recursion(test):
   sum=0
   for element in test:
      if type(element)==type([]):
         sum=sum+recursion(element)
      else:
         sum=sum+element
   return sum   
   
print(recursion([1, 2, [3,4], [5,6]]))
