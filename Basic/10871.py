# 10871 : X보다 작은 수

n, x = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n) :
  if A[i] < x :
    print(A[i], end=' ')
