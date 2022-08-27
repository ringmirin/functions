# # write a python program to print 1-10 and call function to print even or odd 


def fun(n):
   i=0
   list1=[]
   while i<=n:
      a=i
      list1.append(a)
      i+=1
   return(list1)
def fun2(list1):
   i=0   
   while i<len(list1):
      if list1[i]%2==0:
         print("even")
      else:
         print("odd")
      i+=1
n=int(input("enter the number: "))
print(fun(n))
fun2(fun(n))