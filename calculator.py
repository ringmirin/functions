x=int(input("enter the number: "))
y=int(input("enter the number: "))

def addition(n1,n2):
   print(n1+n2)
def product(n1,n2):
   print(n1*n2)
def subtraction(n1,n2):
   print(n1-n2)

def main():
   user=input("enter your choice: ")
   if user=="+":
      addition(x,y)
   if user=="-":
      subtraction(x,y)
   if user=="*":
      product(x,y)
main()





   