# 14889 : 스타트와 링크

from itertools import combinations  # 조합 함수 (순서 상관 X)
import sys  
input = sys.stdin.readline 

n = int(input())
li = []
min = sys.maxsize  # 알아서 최대값으로 초기화됨.

for i in range(n) :
  a =list(map(int, input().split()))
  li.append(a)  # 이차원 배열 생성

index_set = []
for i in range(n) :
  for j in range(i+1, n) :
    index_set = (list(combinations(li[i], 2)))  

#index_set = list(set(index_set))
# 문자열, 숫자, 튜플만 set에 넣어야 중복 제거 가능 -> set(list(data)) 불가능

print(index_set)