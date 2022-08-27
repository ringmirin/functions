### The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to 
### and including the year 200, etc.
def century(year):
   count=0
   while year>0:
      year=year-100
      count+=1
   return count
print(century(1200))
