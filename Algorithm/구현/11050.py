# 11050 : 이항 계수 1

def factorial(n) :      # 팩토리얼 함수 구현
  if n <= 1 :
    return 1
  else :
    return n * factorial(n-1)

n, k = map(int, input().split())        # n, k 입력받기
print(int(factorial(n) / (factorial(k) * factorial(n-k))))    # 조합 nCr 공식 이용

# 조합 공식 nCr 
# n! / (r! * (n-r)!)