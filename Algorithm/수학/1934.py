# 1934 : 최소공배수

t = int(input())      # t 입력받기

for _ in range(t) :
  a, b = map(int, input().split())      # a, b 입력받기
  i = 1               # 새로운 a, b 를 입력받을 때마다 i 를 1로 초기화
  while (True) :
    n = min(a, b)     # n : a, b 중 작은 수 
    m = max(a, b)     # m : a, b 중 작은 수 
    
    if (m * i) % n == 0 :   # m 의 배수를 돌면서 해당 숫자가 n 의 배수에도 성립되면 출력
      print(m*i)          
      break 
    else :
      i += 1