num = list(map(int, input()))

result = 1
for i in num:
  if i <= 1 or result <=1:
    result += i
    continue
  result *= i

print(result)

## 수정
# 1일 때 처리를 안함.. 1은 곱하기X 더하기 수행해야 함.
# 조건문에서 특히 result <=1 신경쓰자.