num = list(map(int, input()))

result = 1
for i in num:
  if i == 0:
    continue
  result *= i

print(result)