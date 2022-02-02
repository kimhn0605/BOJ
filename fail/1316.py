# 1316 : 그룹 단어 체커
# 해결 x

n = int(input("입력 : "))
count = 0


for i in range(n) :
  word = input("알파벳 입력 : ")
  l = len(word)
  for k in range(l) :

    print(word[k])
    a = word.find(word[k], k+1)

      
       
