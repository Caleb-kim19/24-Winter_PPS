import sys

sum = 0
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
  sum += int(sys.stdin.readline().rstrip())
print(sum-n+1)