number=int(input())
if number <=100:
    bonus_points=5
elif number >1000:
    bonus_points=(number*0.1)
else:
    bonus_points=(number*0.2)
if number%2==0:
   add_bonus_point=1
else:
   add_bonus_point=0
if (number%5==0) and (number%10!=0):
   add_bonus_points=2
else:
    add_bonus_points=0
bonus_points_all=bonus_points+add_bonus_points+add_bonus_point
print(f'{bonus_points_all}')

print(float(f'{number+bonus_points_all}'))