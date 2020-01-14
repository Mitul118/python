t=int(input("Enter no of string"))
c=input("Enter first string:")
g=len(c)
for i in range (0,t):
    b=input("Enter next string:")
    h=len(b)
    if g<h:
        g=h
        c=b
        f=b
    else:
        f=c


print(f)
        
    
