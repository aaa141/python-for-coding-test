from itertools import combinations

n, m = map(int, input().split())
k = list(map(int, input().split()))

a=[]
count = 0
for c in combinations(k, 2):
  if len(set(c)) == 1:
    continue
  else:
    count += 1


print(count)