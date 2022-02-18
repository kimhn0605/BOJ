# 11399 : ATM

n = int(input())        # n 입력받기
arr = list(map(int, input().split()))     # 각 사람이 돈 인출하는 데 걸리는 시간 입력받기
arr.sort()      # arr 배열 -> 오름차순 정렬

time = []
value = 0       

for i in range(n) :       # n 만큼 반복
  value += arr[i]         # value : 각 사람이 인출하는 데 걸리는 시간
  time.append(value)      # time : value 값들의 모임
  
print(sum(time))          # 걸리는 시간의 합 출력

## 예시 입력 : 3, 1, 4, 3, 2
# 오름차순 정렬 -> 1, 2, 3, 3, 4
# 각 사람이 인출하는 데 걸리는 시간 -> 1, 3, 6, 9, 13 ==> 각 value 를 time 배열에 추가
# 각 사람이 인출하는 데 걸리는 시간의 합 -> 1 + 3 + 6 + 9 + 13 = 32 ==> sum(time)
