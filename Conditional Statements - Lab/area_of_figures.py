#Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й. Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle). На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle).

#· Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му

#· Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му

#· Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга

#· Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея

#Резултатът да се закръгли до 3 цифри след десетичната запетая.
from math import pi
fig=str(input())
if fig=='square':
    sq_dul=float(input())
    lice_sq=float(sq_dul*sq_dul)
    print(float(round(lice_sq,3)))
elif fig=='rectangle':
    a_rect=float(input())
    b_rect=float(input())
    lice_rect=float(a_rect*b_rect)
    print(float(round(lice_rect,3)))
elif fig=='circle':
    a_circ=float(input())
    r_circ=float(pi*(a_circ*a_circ))
    print(float(round(r_circ,3)))
elif fig=='triangle':
    a_tri=float(input())
    h_tri=float(input())
    lice_tri=(float((a_tri/2)*h_tri))
    print(float(round(lice_tri,3)))
