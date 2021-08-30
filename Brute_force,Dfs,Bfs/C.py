# 1157 : 단어 공부

n = list(map(str, input()))
count = 0
arr=[]
for i in range(len(n)) :
  for j in range(i+1, len(n)) :
    if n[i] == n[j] :
      arr.append(n[i])

# 무슨 알파벳이 겹치는 지는 알아냈는데 그 후로 모르겠음
# for i in range(len(arr)) :
#   for j in range(i+1, len(arr)) :
#     if arr[i] == arr[j] :
#       count += 1
print(arr)