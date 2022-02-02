# 10870 : 피보나치 수 5

num = int(input())
if num == 0 :
  sum = 0
elif num == 1 :
  sum = 1
else : 
  front = 0
  back = 1
  for i in range(1, num) :
    sum = front + back
    front = back
    back = sum
print(sum)
