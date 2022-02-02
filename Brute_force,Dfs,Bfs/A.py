# 3273 : 두 수의 합 

import sys 
input = sys.stdin.readline 

n = int(input())   # 수열 크기
arr = list(map(int, input().split()))  # 수열 입력받기
arr = sorted(arr)  # 오름차순 정렬
x = int(input())  # 목표값
count = 0  # 쌍의 개수

# 이분 탐색 사용
left, right = 0, n-1
while left != right :
  if arr[left] + arr[right] == x :
    count += 1
    left += 1
  elif arr[left] + arr[right] > x :
    right -= 1
  else :
    left += 1
print(count)

# 아래처럼 이중 for문 사용하면 시간 초과 -> while문 사용
# for i in range(n) :
#   head = i
#   for j in range(i+1, n) :
#     tail = j
#     if arr[head] + arr[tail] > x :
#       break
#     elif arr[head] + arr[tail] == x :
#       count += 1
# print(count)