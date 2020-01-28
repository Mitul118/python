t=input("enter any string-")
arr1=[]
arr2=[]
arr3=[]
arr4=[]
for i in t:
    if i.isupper()==True:
        arr1.append(i)
    elif i.islower()==True:
        arr2.append(i)
    elif i.isnumeric()==True:
        arr3.append(i)
    else :
        arr4.append(i)
arr1.sort()
arr2.sort()
arr3.sort()
arr4.sort()
str=""
for i in arr4:
    str=str+i
for i in arr3:
    str=str+i
for i in arr2:
    str=str+i
for i in arr1:
    str=str+i
print(str)
