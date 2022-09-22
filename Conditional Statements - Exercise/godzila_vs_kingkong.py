budget_film=float(input())
sta_num=int(input())
price_wear=float(input())
decor=float(budget_film*0.1)
if sta_num>150:
    price_wear=price_wear-(price_wear*0.1)
need_money=(sta_num*price_wear)+decor
money_left=budget_film-need_money
if need_money>budget_film:
    money_left=money_left*-1
    print('Not enough money!')
    print(f'Wingard needs {money_left:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')