# # In this kata you will create a function that takes in a list and returns a 
# # list with the reverse order.

def reverse_order(list1):
   i=0
   while i<len(list1):
      a=list1[::-1]
      i+=1
   return a
print(reverse_order([2,3,4,5,6]))