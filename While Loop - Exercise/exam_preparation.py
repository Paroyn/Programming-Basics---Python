fail_grade = int(input())
zadacha = input()
count_grades = 0
count_fail = 0
all_grade = 0

while zadacha != 'Enough':
    grade = int(input())
    all_grade += grade
    last_problem = zadacha
    if grade <= 4:
        count_fail += 1
    if count_fail == fail_grade:
        break
    count_grades += 1
    avr_score = all_grade / count_grades
    zadacha = input()
if count_fail == fail_grade:
    print(f'You need a break, {count_fail} poor grades.')
else:
    print(f'Average score: {avr_score:.2f}')
    print(f'Number of problems: {count_grades}')
    print(f'Last problem: {last_problem}')
