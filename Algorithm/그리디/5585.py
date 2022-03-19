# 5585 : 거스름돈 

pay = int(input())             # 지불해야 할 돈
give = 1000 - pay              # 받아야 할 거스름돈 

coin_type = [500, 100, 50, 10, 5, 1]   # 화폐 단위 -> 배수 (그리디로 해결 가능)
count = 0                       # 받을 잔돈의 개수

for coin in coin_type :         # 화폐 단위를 하나씩 돌아가면서
  if give >= coin :             # 받아야 할 거스름돈이 해당 화폐 단위보다 크다면
    count += (give // coin)     # 잔돈의 개수 += (해당 화폐로 나눈 몫)
    give %= coin                # 거스름돈 %= (해당 화폐로 나눈 나머지)

print(count)