import sys

n=int(input())
sum = 0
max_num = -sys.maxsize
for num in range(1,n+1):
    numbers = int(input())
    sum += numbers
    if numbers > max_num:
        max_num = numbers
other_sum_num = sum - max_num
sums = max_num - other_sum_num
if max_num == other_sum_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(sums)}')
