n = int(input())
str_list = input().split()
dict = {}
for x in str_list:
    dict[x] = dict.get(x, 0) + 1
result = sorted(dict.keys(), key = lambda x: (-dict[x], x) )
for str in result:
    print(str, end=" ")