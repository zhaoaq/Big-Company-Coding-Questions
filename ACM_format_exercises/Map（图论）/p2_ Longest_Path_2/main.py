from collections import defaultdict
g = defaultdict(list)
res = 0
def dfs(u, father, depth):
    global res
    res = max(res, depth)
    for x in g[u]:
        if x == father: continue
        dfs(x, u, depth + 1)

n = int(input())
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
dfs(1, 0, 0)
print(res)
