# 11536 : 줄 세우기

# 방법 1) 정렬 이용
n = int(input())                # n 입력받기

result = 'NEITHER'              # 출력할 문구 초기화
li = []                     
copy = []

for _ in range(n) :
  name = input()                # n 개의 이름 입력받기
  li.append(name)               # 원본 리스트에 저장
  copy.append(name)             # 정렬할 리스트에 저장
  
copy.sort()                    # 오름차순 정렬

# 오름차순 검사
for i in range(n) :
  if li[i] == copy[i] :        # 리스트 요소 하나씩 돌면서 확인하고
    if i == n-1 :              # 마지막 요소까지 일치하다면 출력할 문구 INCREASING 으로 변경
      result = "INCREASING"
    else :
      continue
  else :
    break
    
copy.sort(reverse=True)        # 내림차순 정렬

# 내림차순 검사
for i in range(n) :
  if li[i] == copy[i] :        # 리스트 요소 하나씩 돌면서 확인하고
    if i == n-1 :              # 마지막 요소까지 일치하다면 출력할 문구 DECREASING 으로 변경
      result = "DECREASING"
    else :
      continue
  else :
    break
    
print(result)

# 방법 2) 불리언값 이용
n = int(input())                            # n 입력받기
name = [input() for _ in range(n)]          # 리스트에 입력받은 이름 저장

# check 초깃값이 참이라면 오름차순
check = (name[0] < name[1])

for i in range(1, n-1) :                    # 리스트 요소 하나씩 돌아가면서 비교
  if check != (name[i] < name[i+1]) :       # 비교값이 기존 check 값과 동일하지 않다면 
    print("NEITHER")                        # NEITHER 출력 후 프로그램 종료
    quit()                                  
    
if check :                                  # check 값이 True 라면 INCREASING 출력
  print("INCREASING")
else :                                      # check 값이 False 라면 DECREASING 출력
  print("DECREASING")

