musala = 0
monblan = 0
kilim = 0
k_two = 0
everest = 0
groups = int(input())
num_people = 0
for i in range(1, groups + 1):
    count_group = int(input())
    num_people += count_group
    if count_group <= 5:
        musala += count_group
    elif count_group > 5 and count_group <= 12:
        monblan += count_group
    elif count_group > 12 and count_group <= 25:
        kilim += count_group
    elif count_group > 25 and count_group <= 40:
        k_two += count_group
    else:
        everest += count_group
musala_perc=(musala/num_people)*100
monblan_perc=(monblan/num_people)*100
kilim_perc=(kilim/num_people)*100
k_two_perc=(k_two/num_people)*100
everest_perc=(everest/num_people)*100
print(f'{musala_perc:.2f}%')
print(f'{monblan_perc:.2f}%')
print(f'{kilim_perc:.2f}%')
print(f'{k_two_perc:.2f}%')
print(f'{everest_perc:.2f}%')