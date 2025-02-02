import sys
import math

MAX = 1000000
prime = [True] * (MAX + 1)
prime[0], prime[1] = False, False

for i in range(2, int(math.sqrt(MAX)) + 1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i):
            prime[j] = False

def partitions(n):
    count = 0
    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n - i]:
            count += 1
    return count

input = sys.stdin.read
data = input().splitlines()
T = int(data[0])

for i in range(1, T + 1):
    N = int(data[i])
    print(partitions(N))