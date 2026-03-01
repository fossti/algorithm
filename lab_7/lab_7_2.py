n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    ai = a[i - 1]
    for j in range(1, m + 1):
        if ai == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

lcs_len = dp[n][m]
i, j = n, m
idx_a = []
idx_b = []

while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        idx_a.append(i)
        idx_b.append(j)
        i -= 1
        j -= 1
    else:
        if dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

idx_a.reverse()
idx_b.reverse()

print(lcs_len)
print(*idx_a)
print(*idx_b)