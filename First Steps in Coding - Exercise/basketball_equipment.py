year_tax=float(input())

kecove_40_pec=float(year_tax*0.4)
kecove=float(year_tax-kecove_40_pec)

ekip_20_perc=float(kecove*0.2)
ekip=float(kecove-ekip_20_perc)

ball=float(ekip*0.25)

aksesoari=float(ball*0.2)

taksa=float(year_tax+kecove+ekip+ball+aksesoari)
print(taksa)