def count_lion_arrangements(N):
    MOD = 9901

    if N == 1:
        return 3

    dp = [0] * (N + 1)
    dp[1] = 3
    dp[2] = 7

    for i in range(3, N + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % MOD

    return dp[N]

N = int(input())
print(count_lion_arrangements(N))