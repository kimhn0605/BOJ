# 1158 : 요세푸스 문제

# 방법 1) 데크 사용

from collections import deque         # 데크 임포트

n, k = map(int, input().split())      # n, k 입력받기
deq = deque()           # 데크 생성

result = []             # 요세푸스 순열 (출력할 값)
point = k - 1           # 차례대로 삭제할 인덱스 번호

for i in range(n) :     # 1번 ~ N 번 지정
  deq.append(i+1)
  
while len(deq) != 0 :   # deq 배열 내부의 값이 존재할 때까지
  deq.rotate(-point)    # -point 값만큼 왼쪽으로 회전
  result.append(str(deq.popleft()))     # deq 배열의 맨 왼쪽 요소를 문자열로 반환한 후 삭제
  
# 출력 형태 지정
# 문자열 메서드 join 을 사용하기 위해 삭제할 요소를 문자열로 변환했던 것
print("<", ", ".join(result), ">", sep='')

# -----------------------------------------------------------------------

# 방법 2

n, k = map(int, input().split())        # n, k 입력받기
arr = [0] * n           # n 개의 원소를 가진 배열 만들기
result = []             # 요세푸스 순열 (출력할 값)
point = k-1             # 차례대로 삭제할 인덱스 번호

for i in range(n) :     # 1번 ~ N 번 지정
  arr[i] = i+1
  
while len(arr) != 0 :   # arr 배열 내부의 값이 존재할 때까지
  result.append(arr.pop(point))       # result 배열에 요세푸스 순열 추가
  point += (k-1)                      # 삭제할 인덱스 번호 업데이트
  
  while point >= len(arr) :           # 만약 point 가 arr 배열 내부에 존재하는 인덱스값보다 크다면
    point -= len(arr)                 # point 가 유효한 인덱스를 가리킬 때까지 point 값 감소
    if len(arr) == 0 :                # 만약 arr 배열 내부 원소가 없다면 (마지막 원소 pop 이후에 while 문 들어온 경우)
      break                           # while 문 탈출
    
print("<", end="")  
        
for i in range(len(result)) :
  # 출력 형태 지정 -> 요세푸스 순열 차례대로 출력
  if i != len(result)-1 :
    print(result[i], end=', ')
  else :
    print(result[i], ">", sep="")

# 빈 리스트로 만들면 인덱스 지정해서 값 넣을 수 없음.
# arr = []
# for i in range(n) :
#    arr[i] = i         (X)
#    arr.append(i)      (O)
