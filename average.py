def average(n):
   i=0
   sum=0
   av=0
   while i<len(n):
      sum+=n[i]
      
      i+=1
   av=sum/len(n)
   return av
print(average([100, 40, 34, 57, 29, 72, 57, 88]))