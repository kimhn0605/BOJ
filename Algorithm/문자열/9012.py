# 9012 : 괄호 ★

t = int(input())            # t 입력받기

for i in range(t) :         # t 개수만큼 반복
  sum = 0
  value = list(input())     # 괄호 입력받기
  
  for i in range(len(value)):     # 괄호 개수만큼 반복
    if value[i] == '(' :          # 시작 괄호이면 +1     
      sum += 1
    elif value[i] == ')' :        # 종료 괄호이면 -1
      sum -= 1
      
    # 조건 3 만족 여부  
    if sum < 0 :                # sum 값이 음수라면 (종료 괄호 개수가 더 많다면)
      print("NO")               # "NO" 출력하고 break
      break
      
  # 조건 1 만족 여부
  if sum == 0 :                 # sum 값이 0 이면
    print("YES")                # "YES" 출력
  elif sum > 0 :                # sum 값이 양수라면 (시작 괄호 개수가 더 많다면) 
    print("NO")                 # "NO" 출력
    
## 조건
# 1. 시작 괄호 개수 == 종료 괄호 개수
# 2. 처음엔 시작 괄호로, 끝은 종료 괄호로 끝나야 함. (3번과 같은 맥락)
# 3. 종료 괄호는 이전까지 나왔던 시작 괄호 개수보다 같거나 작아야 함.