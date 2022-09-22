shir = int(input())
dulj = int(input())
visoch = int(input())
kb_svobodno = shir * dulj * visoch
count_box = int(input())
kb_have = 0
while count_box != "Done":
    cur_box = int(count_box)
    kb_have += cur_box
    if kb_have > kb_svobodno:
        break
    count_box = input()
diff = abs(kb_svobodno - kb_have )
if kb_have > kb_svobodno:
    print(f'No more free space! You need {diff} Cubic meters more.')
if count_box == "Done":
    print(f'{diff} Cubic meters left.')
