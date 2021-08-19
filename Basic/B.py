# 1110

x = int(input())
result = 0
count = 0
80  + 6 + 8

def Count(x) :
  s = (int(x / 10) + (x- int(x/10)*10))
  result = (x-(int(x / 10))*10)*10 + (s-(int(s/10)*10))
  #print(result)
  return result

while True :
  if (count == 0) :
    result = Count(x)
    count += 1
  elif (result == x) :
    break
  elif (result != x) :
    result = Count(result)
    count += 1

print(count)
