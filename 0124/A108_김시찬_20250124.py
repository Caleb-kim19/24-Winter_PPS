def is_palindromic_sum(n):
    reversed_n = int(str(n)[::-1])
    total = n + reversed_n
    return str(total) == str(total)[::-1]

t = int(input())
for _ in range(t):
    n = int(input())
    if is_palindromic_sum(n):
        print("YES")
    else:
        print("NO")