# 2577 : 숫자의 개수

result = 1
for i in range(3) :
  num = int(input())
  result *= num
result = list(map(int, str(result)))
for i in range(10) :
  count = 0
  for j in range(len(result)) :
    if i == result[j] :
      count += 1
  print(count)
    