def fun(n):
   i=0
   list1=[]
   while i<=n:
      b=i
      list1.append(b)
      i+=1
   return list1
n=int(input("enter: "))
def fun2(list1):
   i=0
   while i<len(list1):
      if list1[i]%2==0:
         print(i,"=","even")
      else:
         print(i,"=","odd")
      i+=1
print(fun(n))
fun2(fun(n))