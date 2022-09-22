age=int(input())
wash_machine_price=float(input())
toys_price=int(input())
money=0
money_odd=0
toys=0

for n in range(1,age+1):
    if n % 2 == 0:
        money+=10
        money_odd+=money
        money_odd-=1
    else:
        toys+=1
toys_money=toys*toys_price
total_money=toys_money+money_odd
diff=abs(wash_machine_price-total_money)
if total_money >= wash_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')