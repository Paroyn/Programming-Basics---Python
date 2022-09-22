budget=float(input())
season=str(input())
count_fisher=int(input())
price_rent=0
if season=='Spring':
    price_rent=3000
elif season=='Summer' or season=='Autumn':
    price_rent=4200
elif season=='Winter':
    price_rent=2600

if count_fisher <= 6:
    price_rent=price_rent * 0.90
elif count_fisher <= 11 and count_fisher>=7:
    price_rent=price_rent * 0.85
else:
    price_rent = price_rent * 0.75
if count_fisher%2==0:
    if season !='Autumn':
        price_rent=price_rent*0.95

diff=abs(budget-price_rent)

if budget>=price_rent:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')