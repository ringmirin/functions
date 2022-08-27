# Write a function named add_numbers which takes two numbers as arguments and then prints their sum. 
# The name of the arguments should be number1 and number2.

def add_numbers(num1,num2):
   print(num1+num2)
add_numbers(56,12)
   



# Write a function named add_numbers_list which takes 2 lists of two integers and then prints 
# the sum of the integers with the same position.

def add_numbers():
   num1=[20,30,10]
   num2=[40,50,60]
   sum=0
   i=0
   while i<len(num1):
         sum=num1[i]+num2[i]
         print(sum)
         i+=1
add_numbers()


