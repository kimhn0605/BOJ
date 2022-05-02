# 14726 : 신용카드 판별

t = int(input())              # t : 테스트 케이스 개수

for _ in range(t) :
  n = input()                 # 숫자 입력받기
  result = 0  
  
  for i in range(1, len(n)+1) :
    if i % 2 == 0 :           # 1번 조건 수행
      temp = int(n[-i])
      temp *= 2
      
      if temp >= 10 :         # 2번 조건 수행
        temp = (temp // 10 + temp % 10)
        
      result += temp          # 짝수 번째 - 3번 조건 수행
      
    else :
      result += int(n[-i])    # 홀수 번째 - 3번 조건 수행
      
  if result % 10 == 0 :       # 4번 조건에 해당하면 T 출력
    print("T")  
  else :                      # 4번 조건에 해당하지 않으면 F 출력
    print("F")