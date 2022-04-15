# 1010 : 다리 놓기

def factorial(n) :          # 재귀 팩토리얼 함수 구현
  if n == 0 or n == 1 :
    return 1
  else :
    return n * factorial(n-1)

test = int(input())         # 테스트 케이스 입력받기 

for _ in range(test) :
  n, m = map(int, input().split())      # n, m 입력받기
  result = int(factorial(m) / ((factorial(m-n) * factorial(n))))      # 조합 공식 mCn
  print(result)

# 동쪽 m 개의 사이트 중에서 순서 상관없이 서쪽 n 개 사이트를 고르면 되는 문제 -> 조합
# 조합 공식 :  C(n, r) = n! / ((n-r)! * r!)