s = input()

count = 0
tmp = -1

for i in s:
  if tmp != i:
    count +=1
  tmp = i

print(count//2)