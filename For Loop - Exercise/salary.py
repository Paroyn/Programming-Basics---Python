count_tabs=int(input())
salary=int(input())
for i in range(1, count_tabs + 1):
    if salary>0:
        tab=str(input())
        if tab == "Facebook":
            salary -= 150
        elif tab == "Instagram":
            salary -= 100
        elif tab == "Reddit":
            salary -= 50
    else:
        break
if salary > 0:
    print(salary)
else:
    print('You have lost your salary.')