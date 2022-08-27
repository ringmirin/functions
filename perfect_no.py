# Define a function named perfect() which takes one argument(integer) and checks if it is a perfect number 
# or not. Now use this code to write a program that prints all the perfect numbers between 1-1000

def perfect():
   num=int(input("Enter the number: "))
   i=1
   sum=0
   while i<num:
      if (num%i==0):
         sum=sum+i
      i=i+1
   if sum==num:
      return("perfect")
   else:
      return("not")
print(perfect())
   



def perfect():
   for n in range(1,1000-1):
      sum=0
      for x in range(1,n-1):
         if n%x==0:
            sum+=x
      if sum==n:
         print(n)
perfect()
         
 
