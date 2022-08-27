def grow(arr):
   a=1
   i=0
   while i<len(arr):
      a*=arr[i]
      i+=1
   return a
print(grow([1,2,3,4]))
   
   