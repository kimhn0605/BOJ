# 11866 : 요세푸스 문제 0

# 방법 1

n, k = map(int, input().split())      # n, k 입력받기
li = list(range(1, n+1))              # 1번 ~ n번까지의 리스트 생성
print("<", end="")
i = 0                             

while len(li) > 1 :     # 리스트 요소가 2개 이상일 동안 반복
  i += k
  
  if i > len(li) :      # 인덱스 i 가 리스트 크기보다 크다면
    i %= len(li)        # 리스트 크기로 나눈 나머지만큼 인덱스 감소
    if i == 0 :         # 리스트 크기로 나눴을 때 딱 나누어떨어졌다면
      i += len(li)      # 다시 리스트 크기만큼 증가 (어차피 아래에서 -1하니까 범위 초과 x)
      
  i -= 1             
  print(str(li.pop(i)), end=", ")       # 리스트에서 i 번째 인덱스 제거
  
print("{}>".format(str(li.pop())))      # 마지막 남은 원소 제거하면서 출력
  
# 방법 2
n, k = map(int, input().split())      # n, k 입력받기
li = list(range(1, n+1))              # 1번 ~ n번까지의 리스트 생성
i = k-1                               # 리스트에서 삭제할 인덱스 번호 (k-1)

print("<", end="")

while (True) :
  # 출력 형식 지정 및 i 번째 인덱스 제거
  if len(li) == 1 :                  
    print(li.pop(i), end=">")         
  else :
    print(li.pop(i), end=", ")
    
  i += (k-1)                # 다음으로 삭제할 요소 가리키기 위해 k-1 만큼 인덱스 증가 
  
  if len(li) == 0 :         # 남아있는 요소 개수가 0 이라면 while 문 탈출
    break   
  while(True) :             # 남아있는 요소 개수가 0 이 아닐 때 
    if i >= len(li) :       # 인덱스 i 가 리스트 크기와 같거나 크다면
      i -= len(li)          # 리스트 크기만큼 인덱스 감소
    else :                  # 인덱스 i 가 리스트 크기보다 작아졌다면 while 문 탈출
      break         
