import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))