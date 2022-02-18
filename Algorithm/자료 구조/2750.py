# 2750 : 수 정렬하기

num = int(input())
li = []
for i in range(num) :
  a = int(input())
  li.append(a)
 
for x in sorted(li) :
  print(x)