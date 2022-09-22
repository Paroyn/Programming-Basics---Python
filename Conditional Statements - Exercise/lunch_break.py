import math
ser=str(input())
ep_prod=int(input())
break_prod=int(input())
lunch_prod=break_prod/8
relax_prod=break_prod/4
time_for_ep=break_prod-(lunch_prod+relax_prod)
left_time=math.ceil(abs(break_prod-(lunch_prod+relax_prod+ep_prod)))
if time_for_ep >= ep_prod:
    print(f'You have enough time to watch {ser} and left with {math.floor(left_time} minutes free time.')
else:
    print(f"You don't have enough time to watch {ser}, you need {left_time} more minutes.")