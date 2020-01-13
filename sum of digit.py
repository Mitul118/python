n=int(input("Enter a number:"))
total=0
while(n>0):
    a=n%10
    total=total+a
    n=n//10
print("The total sum of digits is:",total)
