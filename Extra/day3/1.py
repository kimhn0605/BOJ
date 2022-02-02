# 2309 : 일곱 난쟁이

num = []
for i in range(9) :
  a = int(input())
  num.append(a)

extra = sum(num) - 100
for i in range(len(num)) :
  for j in range(i+1, len(num)) :
    if (num[i] + num[j]) == extra :
      del num[i]
      del num[j-1]
      break
num = sorted(num)
for i in range(len(num)) :
  print(num[i])