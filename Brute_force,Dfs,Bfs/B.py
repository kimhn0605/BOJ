# 1806 : 부분합

# 답은 맞게 나오는 것 같은데 시간 초과,,
import sys 
input = sys.stdin.readline 

min = 0
count = []

n, s = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n) :
  sum = 0
  sum = arr[i]
  for j in range(i+1, n) :
    sum += arr[j]
    if sum >= s :
      count.append(j-i+1)
      break
count = sorted(count)
print(count[0])