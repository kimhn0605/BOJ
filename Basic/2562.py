# 2562 : 최댓값

arr = []
for i in range(9) :
  n = int(input())
  arr.append(n)
  if i == 0 :
    max = arr[0]
    index_num = i+1
  else :
    if arr[i] > max :
      max = arr[i]
      index_num = i+1
print(max, index_num, sep="\n")