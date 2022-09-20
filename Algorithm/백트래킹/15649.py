# 15649 : N과 M (1)

from itertools import permutations        # 순열 라이브러리

n, m = map(int, input().split())          # n, m 입력받기
li = [i for i in range(1, n+1)]           # 1 ~ n 까지의 자연수 집합

for per in permutations(li, m) :          # 순열 결과를 하나씩 순회하면서
  per = str(per)                          # 문자열 변환 후 
  print(''.join(per.split(","))[1:-1])    # 형식에 맞게 출력