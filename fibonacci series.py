n=int(input("no of terms required:"))
n1=0
n2=1
count=0

if n<=0:
    print("please enter a valid number")
elif n==1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("fibonacci sequence:")
    while count<n:
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count+=1
