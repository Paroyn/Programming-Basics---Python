import math
rec=float(input())
lenth=float(input())
time_s_1m=float(input())
time=time_s_1m*lenth
slow=math.floor(lenth/15)*12.5
all_time=time+slow
if rec>all_time:
    print(f'Yes, he succeeded! The new world record is {all_time:.2f} seconds.')
else:
    left_time=(abs(rec-all_time))
    print(f'No, he failed! He was {left_time:.2f} seconds slower.')