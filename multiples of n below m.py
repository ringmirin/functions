# Find the sum of all multiples of n below m

def multiples():
   if n<0 or m<0:
      return "invalid"
   else:
      i=1
      sum=0
      while i<m:
         if i%n==0:
            print(i)
            sum=sum+i
         i+=1
      return sum
   
n=int(input("enter the starting number n: "))
m=int(input("enter the ending number m: "))
print(multiples())      
 




   
         
