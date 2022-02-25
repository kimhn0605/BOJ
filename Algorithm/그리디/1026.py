# 1026  : 보물

n = int(input())        # n 입력받기
a = list(map(int, input().split()))       # a 배열 입력받기
b = list(map(int, input().split()))       # b 배열 입력받기

a.sort(reverse = True)        # a : 내림차순 정렬 
b.sort()                      # b : 오름차순 정렬

result = 0

for i in range(n) :           # n 만큼 반복
  result += (a[i] * b[i])     # 내림차순 정렬된 
  
print(result)

## 합이 제일 작으려면 (a의 최댓값 * b의 최솟값)
# ex) a : 1 1 1 6 0 -> 6 1 1 1 0
#     b : 2 7 8 3 1 -> 1 2 3 7 8
# result = 6*1 + 1*2 + 1*3 + 1*7 + 0*8 = 18