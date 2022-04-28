# 2675 : 문자열 반복

n = int(input())        # 테스트 케이스 수 입력받기

for _ in range(n) :
  result = ''
  
  num, word = input().split()     # 반복할 숫자와 단어 입력받기
  num = int(num)
  
  for j in word :       # 단어를 하나씩 순회하면서
    result += j * num   # 입력한 숫자만큼 문자를 곱해서 result 에 이어붙이기
    
  print(result)
