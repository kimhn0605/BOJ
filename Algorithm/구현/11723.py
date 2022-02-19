# 11723 : 집합

import sys                        # 시간 초과 해결
m = int(sys.stdin.readline())     # m 입력받기
s = set()                         # 빈 집합 (set) 객체 생성

for _ in range(m) :               # m 개수만큼 반복
  word = sys.stdin.readline().split()      # 명령어와 값 입력받기 
  
  if len(word) == 1 :             # 명령어만 입력받았을 때 (all, empty)
    if word[0] == 'all' :         # 명령어가 all 이라면
      s = set([i for i in range(1, 21)])  # 1~20 으로 원소 교체
    else :                        # 명령어가 empty 라면 
      s = set()                   # 공집합으로 교체
      
  else :                                  # 명령어와 값 모두 입력받았을 때 (add, remove, toggle, check)
    func, val = word[0], int(word[1])     # 'func' : 명령어, 'val' : 정수형으로 바꾼 값
    
    if func == 'add' :                    # 명령어가 add 라면 원소 추가
      s.add(val)                          # add 메서드 -> 중복되는 값은 에러 없이 무시
    elif func  == 'remove' :              # 명령어가 remove 라면 원소 삭제
      s.discard(val)                      # discard 메서드 -> 해당 원소가 없다면 에러 없이 무시                              
    elif func  == 'toggle' :              # 명령어가 toggle 일 때
      if val in s :                       # 집합 s에 원소가 있으면 삭제
        s.discard(val)
      else :                              # 집합 s에 원소가 없으면 추가
        s.add(val)  
    else :                                # 명령어가 check 일 때
      print(1 if val in s else 0)         # 집합 s에 원소가 있으면 1, 없으면 0 출력
      
## set.discard() 메서드 -> 해당 원소가 없어도 에러 X
## set.remove() 메서드  -> 해당 원소가 없으면 에러 발생