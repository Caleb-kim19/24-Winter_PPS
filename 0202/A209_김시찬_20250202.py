A, B = map(int, input().split())
m = int(input())
digits = list(map(int, input().split()))

decimal = 0
for i in range(m):
    decimal += digits[i] * (A ** (m - i - 1))

result = []
while decimal > 0:
    result.append(decimal % B)
    decimal //= B

print(*reversed(result))