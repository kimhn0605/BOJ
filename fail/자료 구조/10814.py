# 10814 : 나이순 정렬

n = int(input("반복할 수 입력 : "))
li = {}
for i in range(n) :
  age, name = map(str, input("입력 : ").split())
  li = {"age" : age, "name" : name}
  print(li)
  li = sorted(age)
