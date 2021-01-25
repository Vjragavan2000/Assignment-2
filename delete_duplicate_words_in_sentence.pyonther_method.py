a=str(input("Eter the string:"))
b=a.split(' ')
c=[]
for each in b:
	if each not in c:
		c.append(each)
print(" ".join(c))
