def sum_of_sequence(a, b):
    sequence = []
    n = 1

    while len(sequence) < b:
        sequence.extend([n] * n)
        n += 1

    return sum(sequence[a-1:b])

a, b = map(int, input().split())
print(sum_of_sequence(a, b))