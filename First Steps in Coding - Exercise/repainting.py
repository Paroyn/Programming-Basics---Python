nailon_kv=float(input())
boq_lit=float(input())
razreditel=float(input())
hours_maistori=float(input())
torbichki=float(0.4)
#Предпазен найлон - 1.50 лв. за кв. метър
#Боя - 14.50 лв. за литър
#Разредител за боя - 5.00 лв. за литър

nailon_cqla_suma=float(nailon_kv*1.5)
nailon_dopalnitelno=float(2*1.5)
boq_cqla_suma=float(boq_lit*14.5)
razreditel_cqla_suma=float(razreditel*5)
ten_perc_boq=boq_cqla_suma*(10/100)

cqla_suma=float(nailon_cqla_suma+boq_cqla_suma+razreditel_cqla_suma+nailon_dopalnitelno+ten_perc_boq+torbichki)
za_boqdjiite_na_chas=float(cqla_suma*(30/100))
obshto_boqdjii=float(za_boqdjiite_na_chas*hours_maistori)
vsicho=float(nailon_cqla_suma+nailon_dopalnitelno+boq_cqla_suma+razreditel_cqla_suma+ten_perc_boq+obshto_boqdjii+torbichki)
print(vsicho)