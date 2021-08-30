# 3009 : 네 번째 점

x_li = []
y_li = []
for i in range(3) :
  x, y = input().split()
  x_li.append(x)
  y_li.append(y)
x_li = sorted(x_li)
y_li = sorted(y_li)

if x_li[1] == x_li[0] :
  nx = x_li[2]
else :
  nx = x_li[0]
if y_li[1] == y_li[0] :
  ny = y_li[2]
else :
  ny = y_li[0]
print(nx, ny)

# 다른 사람 코드 참고

# x = []
# y = []

# for _ in range(3):
#     a,b = map(int, input().split())

#     if a in x:
#         x.remove(a)
#     else:
#         x.append(a)
#     if b in y:
#         y.remove(b)
#     else:
#         y.append(b)

# print(x[0], y[0])