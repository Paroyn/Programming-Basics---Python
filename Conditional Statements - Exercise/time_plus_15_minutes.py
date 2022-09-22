hours=int(input())
min=int(input())

min=min+15

if min>59:
    hours=hours+1
    min=min-60
if hours >23:
    hours=0
if min<9:
    print(f"{hours}:0{min}")
else:
    print(f"{hours}:{min}")
