from collections import defaultdict
g = defaultdict(list)
res = 0

def dfs(u, depth):
    global res
    res = max(res, depth)
    for x in g[u]:
        dfs(x, depth + 1)

n = int(input())
# 注意序号和父节点差2
s = list(map(int, input().split()))
for i, p in enumerate(s):
    g[p].append(i + 2)
dfs(1, 0)
print(res)

