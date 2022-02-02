# 10773 : 제로
# 답 다 맞게 나오는데 왜 틀리는지 모르겠음 대체..ㅠㅠㅠㅠ

import sys  
input = sys.stdin.readline 

k = int(input())
sum = 0
li = []

for i in range(k) :
  num = int(input())
  if num == 0 :
    li.pop(li[len(li)-1]) # remove 쓸 때 중복된 값 중 첫 번째 숫자만 제거된다는 것 주의
  else :
    li.append(num)

#for i in range(len(li)) :
 # sum += li[i]
print(sum(li))
sum(li)