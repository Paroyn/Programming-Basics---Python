fruit=str(input())
day=str(input())
qunt=float(input())
banana=0
apple=0
orange=0
grapefruit=0
kiwi=0
pineapple=0
grapes=0
if day=='Monday' or day=='Tuesday' or day=='Wednesday' or day=='Thursday' or day=='Friday':
   if fruit=='banana':
       fruit=2.50
       sum = qunt * fruit
       print(f'{sum:.2f}')
   elif fruit=='apple':
       fruit=1.20
       sum = qunt * fruit
       print(f'{sum:.2f}')
   elif fruit=='orange':
       fruit=0.85
       sum = qunt * fruit
       print(f'{sum:.2f}')
   elif fruit=='grapefruit':
       fruit=1.45
       sum = qunt * fruit
       print(f'{sum:.2f}')
   elif fruit=='kiwi':
       fruit=2.70
       sum = qunt * fruit
       print(f'{sum:.2f}')
   elif fruit=='pineapple':
       fruit = 5.50
       sum = qunt * fruit
       print(f'{sum:.2f}')
   elif fruit=='grapes':
       fruit=3.85
       sum = qunt * fruit
       print(f'{sum:.2f}')
   else:
       print('error')
elif day=='Saturday' or day=='Sunday':
    if fruit == 'banana':
        fruit = 2.70
        sum = qunt * fruit
        print(f'{sum:.2f}')
    elif fruit == 'apple':
        fruit = 1.25
        sum = qunt * fruit
        print(f'{sum:.2f}')
    elif fruit == 'orange':
        fruit = 0.90
        sum = qunt * fruit
        print(f'{sum:.2f}')
    elif fruit == 'grapefruit':
        fruit = 1.60
        sum = qunt * fruit
        print(f'{sum:.2f}')
    elif fruit == 'kiwi':
        fruit = 3.00
        sum = qunt * fruit
        print(f'{sum:.2f}')
    elif fruit == 'pineapple':
        fruit = 5.60
        sum = qunt * fruit
        print(f'{sum:.2f}')
    elif fruit == 'grapes':
        fruit = 4.20
        sum=qunt*fruit
        print(f'{sum:.2f}')
else:
    print('error')
