n = list(map(lambda x: ord(x) ,input()))
n.sort()

s=0
for i in n:
  if i<ord('A'):
    s += int(chr(i))
    continue
  print(chr(i),end="")
print(s)