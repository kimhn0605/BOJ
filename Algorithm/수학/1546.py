# 1546 : 평균

n = int(input())
subject = list(map(int, input().split()))

subject.sort()
sum = 0

for i in range(len(subject)) :
  subject[i] = subject[i] / subject[-1] * 100
  sum += subject[i]
  
print(sum / n)