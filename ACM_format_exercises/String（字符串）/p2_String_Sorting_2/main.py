from functools import cmp_to_key

rank = {}
line = input()

def compare(a, b):
    length = min(len(a), len(b))
    for i in range(length):
        if a[i] != b[i]:
            return rank[a[i]] - rank[b[i]]
    return len(a) - len(b)

for i, letter in enumerate(line):
    rank[letter] = i
n = int(input())
res = []
for x in range(n):
    t = input()
    res.append(t)
res.sort(key = cmp_to_key(compare))
for t in res:
    print(t)