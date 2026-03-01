n = int(input())
if n == 0:
    print(0)
    exit()

val = [0] * (n + 1)
left = [0] * (n + 1)
right = [0] * (n + 1)

for i in range(1, n + 1):
    d, l, r = map(int, input().split())
    val[i] = d
    left[i] = l
    right[i] = r
ans = 0
stack = [(1, 0)]

while stack:
    v, cur = stack.pop()
    if v == 0:
        continue
    cur = cur * 10 + val[v]

    if left[v] == 0 and right[v] == 0:
        ans += cur
    else:
        if right[v] != 0:
            stack.append((right[v], cur))
        if left[v] != 0:
            stack.append((left[v], cur))

print(ans)
