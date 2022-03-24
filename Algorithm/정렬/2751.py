# 2751 : 수 정렬하기 2

## n의 범위 : 최대 100만 (10^6), 시간 제한 2초
# 시간 복잡도 O(NlogN) 까지 가능 -> 1초에 약 2천만 번의 연산 가능
# 이 시간 복잡도에서 할 수 있는 방법은
# 고급 정렬 알고리즘 (병합/퀵/힙 정렬) 또는 기본 정렬 라이브러리 (sorted) 사용

# 방법 1 : 기본 정렬 라이브러리 sort() 이용
n = int(input())            # n 입력받기
li = []

for _ in range(n) :         # n개의 원소 입력받기
  li.append(int(input()))

li.sort()                   # sort 정렬 이용

for i in range(n) :
  print(li[i])
  
# 방법 2 : 병합 정렬 사용
def merge_sort(array) :
  if len(array) <= 1 :
    return array
    
  # 재귀함수를 이용하여 끝까지 분할
  mid = len(array) // 2
  left = merge_sort(array[:mid])
  right = merge_sort(array[mid:])

  # i : left 배열의 인덱스, j : right 배열의 인덱스, k : array 배열의 인덱스
  i, j, k = 0, 0, 0

  # 분할된 배열끼리 비교
  while i<len(left) and j<len(right) :
    if left[i] < right[j] :
      array[k] = left[i]
      i += 1
    else :
      array[k] = right[j]
      j += 1
    k += 1

  # 정렬 중 어느 한쪽의 배열이 먼저 끝났을 때
  if i == len(left) :
    while j < len(right) :
      array[k] = right[j]
      j += 1
      k += 1

  elif j == len(right) :
    while i < len(left) :
      array[k] = left[i]
      i += 1
      k += 1
      
  return array

n = int(input())
li = []

for _ in range(n) :
  li.append(int(input()))

li = merge_sort(li)

for i in li :
  print(i)