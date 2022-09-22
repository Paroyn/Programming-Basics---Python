tip_proj=str(input())
r=int(input())
c=int(input())

if tip_proj=='Premiere':
    cena_bilet=12
    obshta_cena=(r*c)*cena_bilet
    print(f'{obshta_cena:.2f} leva')
if tip_proj=='Normal':
    cena_bilet=float(7.5)
    obshta_cena=(r*c)*cena_bilet
    print(f'{obshta_cena:.2f} leva')
if tip_proj=='Discount':
    cena_bilet=float(5)
    obshta_cena=(r*c)*cena_bilet
    print(f'{obshta_cena:.2f} leva')



