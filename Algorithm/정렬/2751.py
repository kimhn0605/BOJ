# 2751 : 수 정렬하기 2

n = int(input())            # n 입력받기
li = []

for _ in range(n) :         # n개의 원소 입력받기
  li.append(int(input()))

li.sort()                   # sort 정렬 이용

for i in range(n) :
  print(li[i])