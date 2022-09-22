import math
count_torn = int(input())
start_points = int(input())
points_torn = 0
won_torn = 0
for i in range(1, count_torn + 1):
    stage = input()
    if stage == 'W':
        won_torn += 1
        points_torn += 2000
    elif stage == 'F':
        points_torn += 1200
    elif stage == 'SF':
        points_torn += 720
final_points = start_points + points_torn
aver_points = points_torn / count_torn
perc_won = (won_torn/count_torn) * 100
print(f'Final points: {final_points}')
print(f'Average points: {math.floor(aver_points)}')
print(f'{perc_won:.2f}%')
