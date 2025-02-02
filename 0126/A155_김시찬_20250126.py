def solution(price, money, count):
    total_cost = price * count * (count + 1) // 2
    answer = total_cost - money
    
    if answer > 0:
        return answer
    return 0