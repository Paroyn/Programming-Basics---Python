first_seconds=int(input())
secound_seconds=int(input())
thirt_seconds=int(input())

total_seconds=first_seconds+secound_seconds+thirt_seconds
minutes=total_seconds//60
seconds=total_seconds%60
if seconds <=10:
    print(f'{minutes}:0{seconds} ')
else:
    print(f'{minutes}:{seconds} ')

