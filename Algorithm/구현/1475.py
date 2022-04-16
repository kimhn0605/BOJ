# 1475 : 방 번호

import math

n = list(map(int, input()))     # 입력받은 n 을 각 자리별로 리스트에 저장

li = []
count = [0 for _ in range(10)]  # count : 0 ~ 9 개수 각각 카운트할 리스트 

n.sort()     # n 오름차순 정렬

for i in range(10) :            # n 리스트에서 0 ~ 9 숫자 카운트해서 li 에 저장
  li.append(n.count(i))

if li[6] == max(li) or li[9] == max(li) :     # 숫자 6이나 9의 개수가 리스트에서 최댓값이라면
  val = math.ceil((li[6] + li[9])/2)          # 6과 9는 서로 혼용해서 사용 가능하므로 / 2 
  li[6] = val                   # 위 계산식을 변수에 따로 담지 않고 식 그대로 li[6], li[9] 에 저장한다면
  li[9] = val                   # li[9] 에서는 변경된 li[6] 값을 참고하기 때문에 val 에 결과값 저장 후 할당

print(max(li))                  # li 에서 최댓값 => 필요한 세트 개수
  