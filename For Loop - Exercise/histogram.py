num=int(input())
p1=0
p2=0
p3=0
p4=0
p5=0
for numbers in range(num):
    numbers=int(input())
    if numbers<200:
        p1+=1
    elif numbers>=200 and numbers <400:
        p2+=1
    elif numbers>=400 and numbers<600:
        p3+=1
    elif numbers>=600 and numbers<800:
        p4+=1
    else:
        p5+=1
p_one_perc=(p1/num)*100
p_two_perc=(p2/num)*100
p_three_perc=(p3/num)*100
p_four_perc=(p4/num)*100
p_five_perc=(p5/num)*100
print(f'{p_one_perc:.2f}%')
print(f'{p_two_perc:.2f}%')
print(f'{p_three_perc:.2f}%')
print(f'{p_four_perc:.2f}%')
print(f'{p_five_perc:.2f}%')
