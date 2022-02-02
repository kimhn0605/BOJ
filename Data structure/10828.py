# 10828 : 스택

import sys 
input = sys.stdin.readline 

n = int(input())
arr = []

def push(arr, x) :
  arr.append(x)

def pop(arr) :
  if (len(arr) == 0) :
    print("-1")
  else :
    print(arr[len(arr)-1])
    arr.pop(len(arr)-1)

def empty(arr):
  if len(arr) == 0 :
    print("1")
  else :
    print("0")

def top(arr) :
  if len(arr) == 0 :
    print("-1")
  else :
    print(arr[len(arr)-1])

for i in range(n) :
  op = list(map(str, input().split()))
 
  if op[0] == "push" :
    x = int(op[1])
    push(arr, x)
  if op[0] == "pop" :
    pop(arr)
  elif op[0] == "size" :
    print(len(arr))
  elif op[0] == "empty" :
    empty(arr)
  elif op[0] == "top" :
    top(arr)