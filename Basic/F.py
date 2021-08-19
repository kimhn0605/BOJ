# 2581

m = int(input())
n = int(input())

num = []
sum = 0
for k in range(m, n+1) : 
  count = 0
  for i in range(2, k) : 
    if k % i == 0 :
      count += 1 
      break     # break 없으면 for문이 불필요하게 돌아감 -> 시간 초과 오류
  if (count == 0 and k != 1) : 
    num.append(k)
    sum += k

if len(num) == 0 :
  print("-1")
  
else :
  print(sum)
  print(num[0])