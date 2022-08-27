def strong():
   n=int(input("Enter the number: "))
   sum=0
   temp=n
   while temp>0:
      fact=1
      i=1
      digit=temp%10
      while i<=digit:
         fact=fact*i
         i+=1
      sum=sum+fact
      temp//=10
   if n==sum:
      print("strong number")
   else:
      print("not strong number")
strong()


######

def strong():
   num=int(input("Enter the number: "))
   sum=0
   temp=num
   while temp>0:
      fact=1
      digit=temp%10
      for i in range(1,digit+1):
         fact=fact*i
      sum=sum+fact
      temp//=10
   if num==sum:
      print("strong number")
   else:
      print("not strong number")
strong()