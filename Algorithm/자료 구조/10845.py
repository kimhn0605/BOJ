# 10845 : 큐

import sys

n = int(sys.stdin.readline())     # n 입력받기
arr = []    

for i in range(n) :               # n 번만큼 반복해서 명령어 입력받기
  command = sys.stdin.readline().split()      
  func = command[0]               # func : 명령어
  
  if len(command) == 2 :          # push : 명령어와 숫자가 동시에 들어올 때
    arr.append(command[1])        # arr 배열에 원소 추가

  else :                    
    if func == 'pop' :            # 명령어가 pop 일 때
      if len(arr) != 0 :          
        print(arr[0])
        arr.pop(0)
      else :
        print(-1)
        
    elif func == 'size' :         # 명령어가 size 일 때
      print(len(arr))
      
    elif func == 'empty' :        # 명령어가 empty 일 때
      print(1 if len(arr) == 0 else 0)
      
    elif func == 'front' :         # 명령어가 front 일 때
      print(arr[0] if len(arr) != 0 else -1)
      
    elif func == 'back' :          # 명령어가 back 일 때
      print(arr[-1] if len(arr) != 0 else -1)
      
# pop()  : 맨 마지막 원소 삭제
# pop(0) : 맨 처음 원소 삭제