def find_fraction(x):
    n = 1
    while x > n * (n + 1) // 2:
        n += 1

    start = (n - 1) * n // 2
    position = x - start

    if n % 2 == 0:
        numerator = position
        denominator = n - position + 1
    else:
        numerator = n - position + 1
        denominator = position
    
    return f"{numerator}/{denominator}"

x = int(input())
print(find_fraction(x))
