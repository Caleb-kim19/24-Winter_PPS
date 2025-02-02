s = [list(map(int, input().split())) for _ in range(5)]
list = []

for i in range(5):	
	sum = 0
	for j in s[i]:
		sum += j
	list.append(sum)

print(list.index(max(list))+1, max(list))