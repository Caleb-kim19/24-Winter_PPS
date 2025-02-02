max = 0
count = 0
for i in range(4):
  x, y = map(int, input().split())
  count -= x
  count += y
  if(max < count):
    max = count
print(max)