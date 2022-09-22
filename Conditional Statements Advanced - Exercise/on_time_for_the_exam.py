hour_ex = int(input())
min_ex = int(input())
hour_ar = int(input())
min_ar = int(input())
total_min_ex=(hour_ex * 60)+ min_ex
total_min_ar=(hour_ar * 60)+min_ar
diff=abs(total_min_ex - total_min_ar)
if total_min_ex<total_min_ar:
    print('Late')
    if diff>=60:
        hour=diff//60
        min=diff%60
        if min<10:
            print(f'{hour}:0{min} hours after the start')
        else:
            print(f'{hour}:{min} hours after the start')
    else:
        print(f'{diff} minutes after the start')
elif diff==total_min_ar or diff <=30:
    print('On time')
    if diff>=1 and diff <=30:
        print(f'{diff} minutes before the start')
else:
    print('Early')
    if diff>=60:
        hour=diff//60
        min=diff%60
        if min<10:
            print(f'{hour}:0{min} hours before the start')
        else:
            print(f'{hour}:{min} hours before the start')
    else:
        print(f'{diff} minutes before the start')


