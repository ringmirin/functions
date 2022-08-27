numbers = [3, 5, 7, 34, 2, 89, 2, 5]
max_value=max(numbers)
print(max_value)


##2.You have to print the sum of the elements of the given list by using the sum function.

# numbers = [1, 2, 3, 4, 5]
def sum(n):
   sum=0
   for i in n:
      sum=sum+i
   return sum
print(sum([1, 2, 3, 4, 5]))


###Q3. Using sort function sort the given list.

# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# unorder_list.sort()
# print(unorder_list)


###Q4.By using reverse function print the reverse order of the list.

reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
reverse_list.reverse()
print(reverse_list)


###Q5.Use the min function and find the minimun value of the list.

list = [8, 6, 4, 8, 4, 50, 2, 7]
min_value=min(list)
print(min_value)