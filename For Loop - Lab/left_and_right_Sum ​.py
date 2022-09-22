num = int(input())
sum = 0
summ = 0
left_sum=0
right_sum=0
for numbers in range(2 * num):
    cur_num=int(input())
    if numbers<num:
        left_sum+=cur_num
    else :
        right_sum+=cur_num
diff=abs(left_sum-right_sum)
if diff==0:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {diff}')
