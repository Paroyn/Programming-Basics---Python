#Пилешко меню – 10.35 лв.
#Меню с риба – 12.40 лв.
#Вегетарианско меню – 8.15 лв.

chicken_menu=int(input())
fish_menu=int(input())
vegy_menu=int(input())

all_without_desert=float((chicken_menu*10.35)+(fish_menu*12.4)+(vegy_menu*8.15))
desert=float(all_without_desert*0.2)
all=float(all_without_desert+desert+2.5)
print(all)