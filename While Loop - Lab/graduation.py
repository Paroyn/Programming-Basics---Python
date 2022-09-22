
all_ocenki = 0
counts_failed = 0
times_doing = 0
name = str(input())
while True:
    degree = float(input())
    times_doing += 1
    if degree < 4:
        counts_failed += 1
        if counts_failed == 2:
            print(f'{name} has been excluded at {times_doing} grade')
            break
        times_doing -= 1
    else:
        all_ocenki += degree

    if times_doing == 12:
        avr_ocenka = all_ocenki / 12
        print(f'{name} graduated. Average grade: {avr_ocenka:.2f}')
        break




