def min_travel_cost(n, costs):
    total_cost = sum(costs)
    max_cost = max(costs)
    return total_cost - max_cost

n = int(input())
costs = list(map(int, input().split()))

print(min_travel_cost(n, costs))