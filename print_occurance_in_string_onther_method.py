a=str(input("Enter the String:"))
b=str(input("Enter the Character:"))
c=a.count(b)
ans=0
while(c):
	ans=a.index(b,ans)
	print(ans,end=' ')
	ans=ans+1
	c=c-1
print('')
	
