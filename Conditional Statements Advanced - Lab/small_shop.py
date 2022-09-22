prod=str(input())
city=str(input())
quarn=float(input())
price=0
if city=="Sofia":
    if prod=="coffee":
        price=0.50
    if prod=="water":
        price=0.80
    if prod=="beer":
        price=1.20
    if prod=="sweets":
        price=1.45
    if prod=="peanuts":
        price=1.60
elif city == "Plovdiv":
    if prod == "coffee":
        price = 0.40
    if prod == "water":
        price = 0.70
    if prod == "beer":
        price = 1.15
    if prod == "sweets":
        price = 1.30
    if prod == "peanuts":
        price = 1.50
elif city == "Varna":
    if prod == "coffee":
        price = 0.45
    if prod == "water":
        price = 0.70
    if prod == "beer":
        price = 1.10
    if prod == "sweets":
        price = 1.35
    if prod == "peanuts":
        price = 1.55

money=quarn*price
print(f'{money}')

