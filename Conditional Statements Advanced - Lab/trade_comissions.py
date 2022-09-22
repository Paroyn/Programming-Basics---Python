city=str(input())
sells=float(input())
if (city=='Sofia' or city =='Plovdiv' or city=='Varna') and (sells>=0):
    if city=="Sofia" and (sells<=500 and sells>0):
        com=sells*0.05
        print(f'{com:.2f}')
    elif city=="Sofia" and (sells<=1000 and sells>500):
        com=sells*0.07
        print(f'{com:.2f}')
    elif city=="Sofia" and (sells<=10000 and sells>1000):
        com=sells*0.08
        print(f'{com:.2f}')
    elif city=="Sofia" and sells>10000:
        com=sells*0.12
        print(f'{com:.2f}')
    if city=="Varna" and (sells<=500 and sells>0):
        com=sells*0.045
        print(f'{com:.2f}')
    elif city=="Varna" and (sells<=1000 and sells>500):
        com=sells*0.075
        print(f'{com:.2f}')
    elif city=="Varna" and (sells<=10000 and sells>1000):
        com=sells*0.1
        print(f'{com:.2f}')
    elif city=="Varna" and sells>10000:
        com=sells*0.13
        print(f'{com:.2f}')
    if city=="Plovdiv" and (sells<=500 and sells>0):
        com=sells*0.055
        print(f'{com:.2f}')
    elif city=="Plovdiv" and (sells<=1000 and sells>500):
        com=sells*0.08
        print(f'{com:.2f}')
    elif city=="Plovdiv" and (sells<=10000 and sells>1000):
        com=sells*0.12
        print(f'{com:.2f}')
    elif city=="Plovdiv" and sells>10000:
        com=sells*0.145
        print(f'{com:.2f}')
else:
    print('error')

