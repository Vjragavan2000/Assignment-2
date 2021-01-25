numbers=[1,[],2,3,4,[],[1,2,3],[5,6,7],(3,5,7),[],[],[4,5,2]]
a=numbers.count([])
while(a):
	numbers.remove([])
	a=a-1
print(numbers)
