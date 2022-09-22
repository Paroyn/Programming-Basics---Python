days=int(input())
type=str(input())
ocenka=str(input())
nights=days-1
price=0
all_price=0
if type=='room for one person':
    price=18
elif type=='apartment' and days<10:
    price=25
    all_price=price*days
    all_price=all_price*0.70
elif type=='apartment' and days>=10 and days<=15:
    price=25
    all_price=price*days
    all_price=all_price*0.75
    print(all_price)
elif type=='apartment' and days>15:
    price=25
    all_price=price*days
    all_price=all_price*0.50
elif type=='president apartment' and days<10:
    price=25
    all_price=price*days
    all_price=all_price*0.90
elif type=='president apartment' and days>=10 and days<=15:
    price=25
    all_price=price*days
    all_price=all_price*0.85
elif type=='president apartment' and days>15:
    price=25
    all_price=price*days
    all_price=all_price*0.80
if ocenka=='positive':
    all_price=all_price*1.25
elif ocenka=='negative':
    all_price=all_price*0.90