# 18258 : 큐 2

from collections import deque
import sys  
input = sys.stdin.readline 

deq = deque()
n = int(input())

for i in range(n) :
  op = input().split()  # list(map()) 사용하면 시간 초과 에러
  print(op)
  if op[0] == "push" :
    deq.append(int(op[1]))
  elif op[0] == "pop" :
    if (len(deq) == 0) :
     print("-1")
    else :
     print(deq[0])
     deq.popleft()
  elif op[0] == "size" :
    print(len(deq))
  elif op[0] == "empty" :
    if len(deq) == 0 :
      print("1")
    else :
      print("0") 
  elif op[0] == "front" :
    if len(deq) == 0 :
      print("-1")
    else :
      print(deq[0])
  elif op[0] == "back" :
    if len(deq) == 0 :
      print("-1")
    else :
      print(deq[len(deq)-1])
