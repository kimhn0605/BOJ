# 1712 : 손익분기점

a, b, c = map(int, input().split())       # a, b, c 입력받기
n = 1           # 생산하는 대수

if b >= c :     # b >= c 인 경우 손익분기점 X
    print(-1)
else:     
  print(int(a/(c-b)+1))     # 아래 설명 참고
  
# 아래 코드는 시간초과
a, b, c = map(int, input().split())
n = 1

output = a + n*b
input = n*c

while (b < c) :
  if input > output :
    print(n)
    break
  else :
    n += 1
    output += b
    input += c
else :
  print(-1)

# 생산하는 대수가 늘어날 때마다 c와 b의 차이만큼 수입과 비용의 차이가 줄어들게 됨.
# 따라서 a/(c-b) 대 생산했을 때 수입과 비용이 같아지기 때문에 +1부터 수입이 많아지게 됨.
# 파이썬에서 나눗셈 연산을 하면 항상 소수점도 같이 출력 -> int() 이용