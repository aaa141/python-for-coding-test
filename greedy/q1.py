n = int(input())
a = list(map(int, input().split()))
a.sort()

while True:
  for i in range(a[-1]):
    a.pop()
    if len(a)==0:
      break;