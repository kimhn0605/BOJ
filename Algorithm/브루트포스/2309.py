# 2309 : 일곱 난쟁이

li = []

for _ in range(9) :           # 9개의 키 입력받기
  li.append(int(input()))
  
li.sort()                     # 오름차순으로 키 정렬
diff = sum(li) - 100          # diff : 일곱 난쟁이가 아닌 2명의 키를 합한 값

left, right = 0, -1           # left : 처음 인덱스부터 시작, right : 끝 인덱스부터 시작

while (True) :
  if li[left] + li[right] > diff :        # 두 인덱스를 더한 값이 diff 보다 크다면
    right -= 1                            # 오른쪽 인덱스 -= 1
  elif li[left] + li[right] < diff :      # 두 인덱스를 더한 값이 diff 보다 작다면
    left += 1                             # 왼쪽 인덱스 += 1
  else :                                  # 두 인덱스를 더한 값이 diff 라면
    li.pop(right)                         # 해당 오른쪽 인덱스 먼저 삭제 → 작은 인덱스값에 영향 x
    li.pop(left)                          # 해당 왼쪽 인덱스 삭제 
    break

for i in li :
  print(i)