# 7568 : 덩치

n = int(input())
arr = []

for i in range(n) :
  we, he = map(int, input().split())
  arr.append((we, he))  # 키, 몸무게 묶어서 한 번에 배열에 저장

for i in range(n) :
  count = 1  # 각 등수 (항상 1등으로 초기화)
  for j in range(n) :
    if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1] :  # 자신보다 덩치가 크면 등수 +1
      count += 1
  print(count, end= " ")