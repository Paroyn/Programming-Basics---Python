mounth=str(input())
count_days=int(input())
studio=0
apartment=0
if mounth=="May" or mounth=="October":
    studio=50
    apartment=65
    if count_days>7 and count_days<=14:
        studio=studio*0.95
    elif count_days>14:
        studio=studio*0.70
        apartment=apartment*0.90
elif mounth=="June" or mounth=="September ":
    studio=75.20
    apartment=68.70
    if count_days>14:
        studio=studio*0.80
        apartment = apartment * 0.90
elif mounth=="July" or mounth=="August":
    studio=76
    apartment=77
    if count_days>14:
        apartment = apartment * 0.90
sum_stud=studio*count_days
sum_apart=apartment*count_days
print(f'Apartment: {sum_apart:.2f} lv.')
print(f'Studio: {sum_stud:.2f} lv.')