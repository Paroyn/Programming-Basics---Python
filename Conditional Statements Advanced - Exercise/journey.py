budget=float(input())
season=str(input())
spend=0
if budget<=100:
    place='Bulgaria'
    if season=='summer':
        type = 'Camp'
        spend=budget*0.30
    if season=='winter':
        type = 'Hotel'
        spend=budget*0.70

if budget>100 and budget<=1000:
    place='Balkans '
    if season=='summer':
        type = 'Camp'
        spend=budget*0.40
    if season=='winter':
        type = 'Hotel'
        spend=budget*0.80

if budget>1000:
    place='Europe '
    type='Hotel'
    spend=budget*0.9

print(f'Somewhere in {place}')
print(f'{type} - {spend:.2f}')