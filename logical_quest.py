a=int(input("enter the no. :"))
b=int(input(" "))
sum=a+b
diff=a-b
product=sum*diff
print(product)



#######
# input:
#     arfardarb
# Output:
#     3 3 1 1 1
# Explanation:
#     a is repeated 3 times, followed by r which is repeated 3 times. f, d and b 
# occurs only 1 time.   


user=input("enter the string: ")
dict={}
for i in user:
   if i in dict:
      dict[i]+=1
   else:
      dict[i]=1
for x,y in dict.items():
   print(y,end=" ")


#####
user=input("enter the string: ")
dict={}
list1=[]
for i in user:
   if i in dict:
      dict[i]+=1
   else:
      dict[i]=1
for key,value in dict.items():
   dict1=([key,value])
   list1.append(dict1)
print(list1)