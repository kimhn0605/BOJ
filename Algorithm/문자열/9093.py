# 9093 : 단어 뒤집기

# 방법 1) 문자열 슬라이싱 사용
t = int(input())                    # 테스트 케이스 개수 입력받기

for _ in range(t) :                 
  words = list(input().split())     # 공백마다 하나의 원소로서 리스트에 저장
  
  for w in words :                  # 단어 하나씩 순회하면서
    print(w[::-1], end=" ")         # 슬라이싱 이용해서 문자열 뒤집기 
  print()

# 방법 2) reversed() 메서드 사용
t = int(input())

for _ in range(t) :
  words = list(input().split())
  for w in words :
    # reversed() : reversed object 반환하므로 join 함수 이용해서 문자열 반환
    print(''.join(reversed(w)), end= " ")     
  print()