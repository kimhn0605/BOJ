# 11651 : 좌표 정렬하기 2

n = int(input("점 개수 입력 : "))
x_list = []
y_list = []
for i in range(n) :
  x, y = map(int, input().split())
  x_list.append(x)
  y_list.append(y)
print(x_list, y_list)
