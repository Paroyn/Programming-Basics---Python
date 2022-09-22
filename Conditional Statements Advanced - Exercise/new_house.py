type_flo=str(input())
count_flowers=int(input())
budget=int(input())
suma=0
if type_flo=='Roses':
    suma=count_flowers*5
    if count_flowers>80:
        suma=suma*0.90
elif type_flo=="Dahlias":
    suma = count_flowers * 3.80
    if count_flowers > 90:
        suma = suma-(suma*0.15)
elif type_flo=="Tulips":
    suma = count_flowers * 2.80
    if count_flowers > 80:
        suma = suma - (suma * 0.15)
elif type_flo=='Narcissus':
    suma = count_flowers * 3
    if count_flowers < 120:
        suma = suma + (suma * 0.15)
elif type_flo=='Gladiolus':
    suma = count_flowers * 2.50
    if count_flowers < 80:
        suma = suma + (suma * 0.20)
diff=abs(budget-suma)
if budget>=suma:
    print(f'Hey, you have a great garden with {count_flowers} {type_flo} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')