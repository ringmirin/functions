def square(n):
   answer=0
   while (answer+1)**2<n:
      answer+=1
   return answer**2
print(square(81))
