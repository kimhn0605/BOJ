# 4344
import math
c = int(input())

for i in range(c) :
  case_list = list(map(int, input().split()))
  sum = 0
  count = 0
  for k in range(1, len(case_list)) : 
    sum += case_list[k]
  average = sum / (len(case_list)-1)
  for j in range(1, len(case_list)) :
    if case_list[j] > average :
      count += 1
  ratio = count / (len(case_list)-1)
  
  print(format(round(ratio*100, 3), '.3f'), "%", sep='')