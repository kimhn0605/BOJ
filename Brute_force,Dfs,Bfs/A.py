# 3273 : 두 수의 합

import sys 
input = sys.stdin.readline 
n = int(input())
arr = []
count = 0
arr = input().split()
x = int(input())

# 시간 초과 -> sort 정렬해서 이중 for문 대신 while문으로 해결해야 함
for i in range(n) :
  arr[i] = int(arr[i])
  
for i in range(n) :
  head = i
  for j in range(i+1, n) :
    tail = j
    if arr[head] + arr[tail] == x :
      count += 1
print(count)