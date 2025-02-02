c = int(input())
s_list = [list(map(int, input().split())) for _ in range(c)]

for i in range(c):
  avg = (sum(s_list[i]) - s_list[i][0]) / (len(s_list[i]) - 1)
  count = 0
  for j in range(1, len(s_list[i])):
    if (s_list[i][j] > avg):
      count += 1
  result = count / s_list[i][0] * 100
  print(f'{result:.3f}%')
