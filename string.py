txt=input("enter a string:")
x=list(txt)
x[0],x[-1]=x[-1],x[0]
print(" ".join(x))
