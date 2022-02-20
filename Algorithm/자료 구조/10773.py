# 10773 : 제로

k = int(input())          # k 입력받기
arr = []                  # 입력받는 수 저장할 배열

for i in range(k) :       # k 번 만큼 반복
  num = int(input())      # 숫자 입력받기
  
  if num == 0 :           # 입력받은 수가 0 이라면
    arr.pop(-1)           # arr 배열의 가장 마지막 숫자 삭제
  else :                  # 입력받은 수가 0 이 아니라면
    arr.append(num)       # arr 배열에 해당 숫자 추가
    
print(sum(arr))           # 합계 출력