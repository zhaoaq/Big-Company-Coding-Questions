# 有向图 dfs 邻接表
from collections import defaultdict
n = int(input())
g = defaultdict(list)
for x in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)

def dfs(u, depth):
    global res
    res = max(res, depth)
    for x in g[u]:
        dfs(x, depth + 1)
res = 0
dfs(1, 0)
print(res)
