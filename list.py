x=list(map(int,input("Enter the first list of integers:").split()))
y=list(map(int,input("Enter the second list of integers:").split()))
if len(x)==len(y):
 print("List are not the same")
else:
 print("List are different length")
if sum(x)==sum(y):
 print("sum are same")
else:
 print("sum are different")
common=set(x)&set(y)
common=list(common)
print("common value exist",common if common else"no common value")
