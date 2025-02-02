def solution(x):
	answer = True
	sum = 0
	a = x
	l = [10000, 1000, 100, 10, 1]
	for i in l:
		sum += int(a/i)
		a %= i
	if(x%sum == 0):
		answer = True
	else: 
		answer = False
return answer