n = int(input())
a = list(map(int, input().split()))
a.sort()

count = 0
while True:
  for i in range(a[-1]):
    a.pop()

  count += 1
  if len(a)==0:
    break

print(count)
