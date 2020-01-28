t=input("enter the word")
dict={}
for i in t:
	keys = dict.keys()
	if i in keys:
		dict[i]+=1
	else:
		dict[i]=1
print(dict)
