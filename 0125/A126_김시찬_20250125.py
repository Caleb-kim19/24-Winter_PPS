def is_hansu(num):
    num_str = str(num)
    if len(num_str) < 3:
        return True
    diff = int(num_str[1]) - int(num_str[0])
    for i in range(1, len(num_str) - 1):
        if int(num_str[i + 1]) - int(num_str[i]) != diff:
            return False
    return True

def count_hansu(N):
    count = 0
    for i in range(1, N + 1):
        if is_hansu(i):
            count += 1
    return count

N = int(input())
print(count_hansu(N))