def solution(t, p):
    p_length = len(p)
    p_value = int(p)
    count = 0
    for i in range(len(t) - p_length + 1):
        if int(t[i:i+p_length]) <= p_value:
            count += 1
    return count