import sys
input = sys.stdin.readline

S, C = map(int, input().split())
lengths = [int(input()) for _ in range(S)]

start, end = 1, max(lengths)
best_length = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(l // mid for l in lengths)
    
    if count >= C:
        best_length = mid
        start = mid + 1
    else:
        end = mid - 1

total_length = sum(lengths)
used_length = C * best_length
remaining_length = total_length - used_length

print(remaining_length)