def sum_list(list):
 sum=0
 for i in list:
  sum=sum+i
 return sum
n=int(input("Enter the number of items:"))
list=[]
for i in range(n):
 x=int(input("Enter a item:"))
 list.append(x)
print("Sum of list items=",sum_list(list))


