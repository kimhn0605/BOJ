# 2960 : 에라토스테네스의 체

n, k = map(int, input().split())      # n, k 입력받기

li = list(range(n+1))                 # 0 ~ n 까지 들어있는 리스트 선언
result = []                           # 지워지는 수를 차례대로 담을 리스트

for i in range(2, n+1) :              # i는 2 ~ n 까지 반복
  j = 1                               
  while (True) :
    if i*j > n :                      # i * j 가 n 보다 커지면 While 문 탈출
      break 
    
    if i*j not in result :            # i * j (i의 배수) 가 result 리스트에 존재하지 않을 때만 (중복값이 아닌 경우에만)
      result.append(i*j)              # result 에 저장 
    j += 1                            # j 는 1씩 증가하면서 i의 배수를 차례대로 순회

print(result[k-1])                    
    