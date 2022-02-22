# 1874 : 스택 수열 ★

n = int(input())        # n 입력받기
cnt = 1                 # 이번 차례에 스택에 넣을 숫자

stack = []              # 스택에 담긴 숫자 배열
op = []                 # '+', '-' 담을 배열
flag = True             

for i in range(n) :       # n 번만큼 반복
  val = int(input())      # 숫자 입력받기
  
  while cnt <= val :      # while 문 돌면서 입력받은 수까지 스택에 숫자 쌓기
    stack.append(cnt)   
    op.append('+')        # op 배열에 '+' 추가
    cnt += 1            
    
  if stack[-1] == val :   # 스택 최상단 숫자가 현재 입력받은 숫자와 동일하다면
    stack.pop()           # 스택에서 제거하고 op 배열에 '-' 추가
    op.append('-')
    
  else :                  # 스택 최상단 숫자가 현재 입력받은 숫자가 아니라면
    flag = False          # 스택 수열 X

if flag == True :         # 스택 수열인 경우에만
  for i in range(len(op)) :       # op 배열 돌면서 '+', '-' 하나씩 출력
    print(op[i])
else :                    # 스택 수열이 아니라면
  print('NO')             # 'NO' 출력