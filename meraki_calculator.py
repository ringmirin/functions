# create a python program to create a calculator
def add(x,y):
   return x+y
def sub(x,y):
   return(x-y)
def mul(x,y):
   return(x*y)
def div(x,y):
   return(x/y)
def main():
   if operator=="+":
      print(add(numx,numy))
   if operator=="-":
      print(sub(numx,numy))
   if operator=="*":
      print(mul(numx,numy))
   if operator=="/":
      print(div(numx,numy))
numx=int(input("Enter the number: "))
numy=int(input("Enter the number: "))
operator=input("Enter operator sign:")
main()

######
def multiply(x,y):
   i=0
   list=[]
   while i<len(numx):
      z=x[i]*y[i]
      list.append(z)
      i+=1
   print(list)
numx=[2,3,4,5]
numy=[6,7,8,9]
multiply(numx,numy)







