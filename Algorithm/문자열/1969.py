# 1969 : DNA

n, m = map(int, input().split())                 # n, m 입력받기

li = []
result = []                                      # result : Hamming Distance 합이 가장 작은 DNA 가 담긴 리스트
count = 0                                        # count : Hamming Distance 개수

for _ in range(n) :
  word = input()                                 # DNA 입력받고 2차원 배열 형태로 li 에 저장
  li.append(list(word))

for i in range(m) :
  alpha = []            
  for index in range(n) :
    alpha.append(li[index][i])                   # 2차원 배열을 세로로 끊어서 alpha 에 저장
        
  alpha.sort()                                   # 사전 순으로 가장 앞서는 것을 출력하기 위해 먼저 정렬
  maximum = max(alpha, key=alpha.count)          # maximum : 해당 세로줄 중 빈도수가 가장 높은 앒파벳
  
  result.append(maximum)                         # result 에 최종적으로 출력할 알파벳 저장
  count += (n-alpha.count(maximum))              # n - 빈도수가 가장 높은 알파벳 개수 => Hamming Distance 누적 합계

print(''.join(result))                           # result 에 담긴 알파벳 및 Hamming Distance 출력
print(count)