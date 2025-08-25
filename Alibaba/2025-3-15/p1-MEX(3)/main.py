v = []
line = input().strip()
if line:
    row = list(map(int, line[1:-1].split(',')))
    v.append(row)

n, m = len(v), len(v[0])
res = 0

# 遍历所有2*2的子矩阵
for i in range(n-1):
    for j in range(m-1):
        if v[i][j]+v[i+1][j]+v[i][j+1]+v[i+1][j+1] > n*m:
            res += 1

# 输出结果
print(res)