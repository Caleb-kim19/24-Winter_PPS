a = int(input())
b = int(input())
c = int(input())

n = a*b*c
num_list = list(map(int, str(n)))

checked = [0]*10
for i in num_list:
    checked[i] += 1

for i in range(10):
  print(checked[i])