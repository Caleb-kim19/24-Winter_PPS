def solution(number, limit, power):
    total = 0
    for n in range(1, number + 1):
        count = 0
        j = 1
        while j * j <= n:
            if n % j == 0:
                count += 1
                if j != n // j:
                    count += 1
            j += 1
        
        if count > limit:
            total += power
        else:
            total += count
    return total