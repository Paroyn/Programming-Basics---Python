n=int(input())
sum=0
while True:
    cur_num=int(input())
    sum+=cur_num
    if sum>=n:
        print(sum)
        break