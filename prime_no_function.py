user=int(input("Enter the number: "))
def prime():
   i=1
   count=0
   while i<=user:
      if user%i==0:
         count+=1
      i+=1
   if count==2:
      print("prime")
   else:
      print("not prime")
prime()


######
def prime():
   for x in range(2,100+1):
      if x>1:
         for y in range(2,x):
            if x%y==0:
               break
         else:
            print(x)
prime()
# ######
def primeorNot(num):
   if num > 1:
      for i in range(2,num):
         if (num % i) == 0:
            print(num,"is not a prime number")
            break
         else:
            print(num,"is a prime number")
primeorNot(6)





