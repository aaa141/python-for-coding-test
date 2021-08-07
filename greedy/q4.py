from itertools import combinations

n = int(input())
coin = list(map(int, input().split()))
comb = []

for i in range(len(coin) + 1):
    c = combinations(coin, i)
    comb.extend(c)

subsum = []
for i in comb:
    subsum.append(sum(i))

flag = 0
for i in range(max(subsum)):
    if not i in subsum:
        flag = -1
        print(i)
        break;

if flag == 0:
    print(max(subsum) + 1)