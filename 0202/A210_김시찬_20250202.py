T = int(input())

for _ in range(T):
    n = int(input())
    top = list(map(int, input().split()))
    bottom = list(map(int, input().split()))
    
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = top[0]
    dp[0][1] = bottom[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + top[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + bottom[i])

    print(max(dp[n - 1][0], dp[n - 1][1]))