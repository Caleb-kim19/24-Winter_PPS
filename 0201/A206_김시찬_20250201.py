import math

def find_max_D(N, S, A):
    differences = [abs(S - ai) for ai in A]
    gcd_value = differences[0]
    for diff in differences[1:]:
        gcd_value = math.gcd(gcd_value, diff)
    return gcd_value

N, S = map(int, input().split())
A = list(map(int, input().split()))

print(find_max_D(N, S, A))