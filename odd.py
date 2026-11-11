n=input("enter the numbers:")
result=["OVER" if int(num)>100 else int(num) for num in n.split()]
print(result)
 
