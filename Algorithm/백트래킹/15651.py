# 15651 : N과 M (3)

from itertools import product               # 중복 순열 라이브러리

n, m = map(int, input().split())            # n, m 입력받기
li = [i for i in range(1, n+1)]             # 1 ~ n 까지의 자연수 집합

for prod in product(li, repeat=m) :         # 중복 순열 결과를 하나씩 순회하면서
  prod = str(prod)                          # 문자열 변환 후 
  print(''.join(prod.split(","))[1:-1])     # 형식에 맞게 출력