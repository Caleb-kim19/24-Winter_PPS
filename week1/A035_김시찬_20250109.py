t = int(input())
list = [input().split() for _ in range(t)]

for l in list:
	answer = float(l[0])
	for x in l:
		if x == "@":
			answer *= 3
		elif x == "%":
			answer += 5
		elif x == "#":
			answer -= 7
	print(f'{answer:.2f}')