num = [int(input()) for _ in range(10)]
list = []
for x in num:
	n = x % 42
	if(list.count(n)==0):
		list.append(n)
print(len(list))