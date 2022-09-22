price_trip=float(input())
puz=int(input())
doll=int(input())
bear=int(input())
mini=int(input())
truck=int(input())
count_poruchki=puz+doll+bear+mini+truck
puz_n=puz*2.6
doll_n=doll*3
bear_n=bear*4.1
mini_n=mini*8.2
truck_n=truck*2
money=puz_n+doll_n+bear_n+mini_n+truck_n
if count_poruchki >=50:
    money=money-(money/4)
rent=money*0.1
money_all=money-rent
left_money=abs(money_all-price_trip)
if money_all>=price_trip:
    print(f'Yes! {left_money:.2f} lv left.')
else:
    print(f'Not enough money! {left_money:.2f} lv needed.')