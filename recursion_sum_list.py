# Write a Python program to calculate the sum of a list of numbers.

##recursion
def sum(list1):
   if len(list1)==1:
      return list1[0]
   else:
      return list1[0]+sum(list1[1:])
print(sum([1,2,3,4,5]))


