# 15650 : N과 M (2)

from itertools import combinations          # 조합 라이브러리

n, m = map(int, input().split())            # n, m 입력받기
li = [i for i in range(1, n+1)]             # 1 ~ n 까지의 자연수 집합

for comb in combinations(li, m) :           # 조합 결과를 하나씩 순회하면서
  comb = str(comb)                          # 문자열 변환 후 
  print(''.join(comb.split(","))[1:-1])     # 형식에 맞게 출력