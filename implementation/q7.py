n = list(map(int,input()))
mid = len(n)//2

if sum(n[:mid]) == sum(n[mid:]):
  print('LUCKY')
else:
  print('READY')