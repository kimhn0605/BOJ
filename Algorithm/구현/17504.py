# 17504 : 제리와 톰 2

from fractions import Fraction        # 분수 표현 모듈
n = int(input())                      # n 입력받기

a_li = list(map(int, input().split()))      # n 개의 숫자 입력받기
result = a_li[-1]                           # 초기 result 값은 마지막 값

for i in range(2, n+1) :                    # 끝에서부터 차례대로 분수 계산  
  result = a_li[-i] + Fraction(1, result) 

result = 1-Fraction(1, result)
print(result.numerator, result.denominator, sep=" ")    # 분자, 분모 각각 출력