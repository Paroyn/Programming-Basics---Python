sum_steps = 0
input_line = input()
while input_line != "Going home":
    steps = int(input_line)
    sum_steps += steps
    if sum_steps >= 10000:
        break
    input_line = input()
diff=abs(10000 - sum_steps)
if sum_steps >= 10000 and input_line != 'Going home':
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
elif sum_steps < 10000 and input_line != 'Going home':
    print(f'{diff} more steps to reach goal.')
if input_line == "Going home":
    home = int(input())
    sum_steps += home
    diff = abs(10000 - sum_steps)
    if sum_steps < 10000:
        print(f'{diff} more steps to reach goal.')
    else:
        print('Goal reached! Good job!')
        print(f'{diff} steps over the goal!')