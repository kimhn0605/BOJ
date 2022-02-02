# 8958 : OX퀴즈

n = int(input())
for i in range(n) :
  result  = list(input())
  count = 0 # 연속된 "O" 에 한해 더해지는 합계
  sum = 0 # 총 합계
  j = 0
  while result[j] != "X" :
    count += 1    # 연속적인 "O"의 개수
    j += 1
    print(result[j], count, j)
  j += 1
  print(count)