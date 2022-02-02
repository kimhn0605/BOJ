# 1712 : 손익분기점

a, b, c = map(int, input().split())
n = 1    # 손익분기점 (최초로 이익이 발생하는 판매량)

if b < c :
  while n*c <= (a + n*b) :
    n += 1
  print(n)
else :
  print("-1")