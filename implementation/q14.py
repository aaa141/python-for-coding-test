# 치킨 배달
# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())

city = [[0]*n for i in range(n)]
for i in range(n):
    city[i] = list(map(int, input().split()))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        if city[i][j] == 2:
            chicken.append([i, j])

minimun = 1000
for i in combinations(chicken, m):
    s = 0
    for j in home:
        s += min([abs(j[0]-k[0])+abs(j[1]-k[1]) for k in i])
        if minimun < s:
            break
    if s < minimun:
        minimun = s

print(minimun)

