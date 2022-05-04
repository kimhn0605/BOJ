# 11536 : 줄 세우기

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