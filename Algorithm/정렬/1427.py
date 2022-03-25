# 1427 : 소트인사이드

n = list(map(int, input()))
string = ''

for i in n :
  i = int(i)
  
n.sort(reverse = True)

for i in n :
  string += str(i)
  
print(string)