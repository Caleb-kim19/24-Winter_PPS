import sys
input = sys.stdin.readline

N = int(input().strip())
print("SK" if N % 2 == 0 else "CY")