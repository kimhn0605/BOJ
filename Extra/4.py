# 3052
# 틀림..

import sys  
input = sys.stdin.readline 
n = []
result = 0
for i in range(10) :
  n.append((int(input())) % 42)

for i in range(len(n)) :
  count = 0
  for j in range(i+1, len(n)) :
    if n[i] != n[j] :
      count += 1
    if count == (len(n)-j) :
      result += 1
print(result)