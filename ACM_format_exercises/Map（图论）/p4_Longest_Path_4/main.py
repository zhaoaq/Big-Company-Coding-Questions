n = int(input())
res = 0
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = list(map(int, input().split()))
    g[a].append((b, c))

def dfs(u, depth):
    global res
    res = max(res, depth)
    for x in g[u]:
        dfs(x[0], depth + x[1])
dfs(1, 0)
print(res)