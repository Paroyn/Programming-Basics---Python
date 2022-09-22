n_one=int(input())
n_two=int(input())
oper=str(input())
if oper=="+":
    result=n_one+n_two
    if result%2==0:
        print(f'{n_one} {oper} {n_two} = {result} - even')
    elif result%2!=0:
        print(f'{n_one} {oper} {n_two} = {result} - odd')
if oper=="-":
    result=n_one-n_two
    if result%2==0:
        print(f'{n_one} {oper} {n_two} = {result} - even')
    elif result%2!=0:
        print(f'{n_one} {oper} {n_two} = {result} - odd')
elif oper=="*":
    result = n_one * n_two
    if result % 2 == 0:
        print(f'{n_one} {oper} {n_two} = {result} - even')
    elif result % 2 != 0:
        print(f'{n_one} {oper} {n_two} = {result} - odd')
elif oper=="/":
    if n_two==0:
        print(f'Cannot divide {n_one} by zero')
    else:
        result = n_one / n_two
        print(f'{n_one} {oper} {n_two} = {result:.2f}')
elif oper=="%":
    if n_two == 0:
        print(f'Cannot divide {n_one} by zero')
    else:
        result = n_one % n_two
        print(f'{n_one} {oper} {n_two} = {result}')
