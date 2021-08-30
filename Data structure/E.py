# 2941 : 크로아티아 알파벳

n = input()
count = 0

while len(n) != 0 : 
  i = len(n) - 1

  if n[i] == "=" :
    if n[i-1] == "c" or n[i-1] == "s" or n[i-1] == "z" :
      count += 1
      del n[i-1:i+1]

  elif n[i] == "-" :
    if n[i-1] == "c" or n[i-1] == "d" :
      count += 1
      del n[i-1:i+1]
      
  elif n[i] == "j" :
    if n[i-1] == "l" or n[i-1] == "n" :
      count += 1
      del n[i-1:i+1]
      
  elif n[i] == "=" and n[i-1] == "z" and [i-2] == "d" :
    count += 1
    del n[i-2:i+1]
    
  else :
    count += 1
    del n[i]
