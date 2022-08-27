####find the max of three numbers

num1=int(input("enter the number: "))
num2=int(input("enter the number: "))
num3=int(input("enter the number: "))
def max(num1,num2,num3):
   if num1>num2 and num1>num3:
      return (num1,"max")
   elif num2>num1 and num2>num3:
     return (num2,"max")
   elif num3>num1 and num3>num2:
     return (num3,"max")
print(max(num1,num2,num3))




########
num1=int(input("enter the number: "))
num2=int(input("enter the number: "))
num3=int(input("Enter the number: "))
def max(num1,num2,num3):
   if num1>num2 and num1>num3:
      print(num1,"max")
   elif num2>num1 and num2>num3:
     print(num2,"max")
   elif num3>num1 and num3>num2:
     print(num3,"max")
max(num1,num2,num3)


