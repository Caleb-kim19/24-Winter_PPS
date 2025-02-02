s = input().split(" ")
sum = 0
for n in s:
  sum += int(n) ** 2
answer = sum % 10
print(answer)