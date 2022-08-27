def count_sheep(n):
   a=" "
   count=1
   while count<=n:
      a+=str(count) + str("sheep...")
      count+=1
   return a
print(count_sheep(3))



