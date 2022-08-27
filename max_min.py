# write python program to find the maximum and minimum
def max(arr):
   i=0
   max=arr[0]
   while i<len(arr):
      if arr[i]>max:
         max=arr[i]
      i+=1
   return max
def min(arr):
   j=0
   min=arr[0]
   while j<len(arr):
      if arr[j]<min:
         min==arr[j]
      j+=1
   return min
print(max([2,3,5,7,1]))
print(min([2,3,5,7,1]))


