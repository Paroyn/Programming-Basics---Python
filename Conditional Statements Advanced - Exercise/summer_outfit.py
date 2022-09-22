degree=int(input())
time_day=str(input())
if time_day=='Morning' and (degree>=10 and degree<=18):
    obl='Sweatshirt'
    shoe='Sneakers'
elif time_day=='Morning' and (degree>18 and degree<=24):
    obl='Shirt'
    shoe='Moccasins'
elif time_day=='Morning' and degree>=25:
    obl='T-Shirt'
    shoe='Sandals'
elif time_day=='Afternoon' and (degree>10 and degree<=18):
    obl = 'Shirt'
    shoe = 'Moccasins'
elif time_day == 'Afternoon' and (degree>18 and degree<= 24):
    obl ='T-Shirt'
    shoe = 'Sandals'
elif time_day == 'Afternoon' and degree >= 25:
    obl = 'Swim Suit'
    shoe = 'Barefoot'
elif time_day=='Evening' and (degree>10 and degree<=18):
    obl = 'Shirt'
    shoe = 'Moccasins'
elif time_day == 'Evening' and (degree > 18 and degree <= 24):
    obl = 'Shirt'
    shoe = 'Moccasins'
elif time_day == 'Evening' and degree >= 25:
    obl = 'Shirt'
    shoe = 'Moccasins'
print(f"It's {degree} degrees, get your {obl} and {shoe}.")
