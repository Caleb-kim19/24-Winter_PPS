n = int(input())
x = list(map(int, input().split()))

y_fee = 0
m_fee = 0
for i in range(n):
	y_fee += 10*(int(x[i]/30)+1)
	m_fee += 15*(int(x[i]/60)+1)

if(y_fee < m_fee):
	print("Y", y_fee)
elif(y_fee == m_fee):
		print("Y M", y_fee)
else:
	print("M", m_fee)