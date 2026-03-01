MOD = 10**9 + 7

def pow_mod(a, n):
    if n == 0:
        return 1
    half = pow_mod(a, n // 2)
    res = (half * half) % MOD
    if n % 2 == 1:
        res = (res * (a % MOD)) % MOD
    return res

a_str, n_str = input().split()
a = int(a_str)
n = int(n_str)

result = pow_mod(a, n)
print(result)