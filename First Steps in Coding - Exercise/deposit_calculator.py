dep_sum=float(input())
srok=int(input())
god_procent=float(input())

per_year=dep_sum*(god_procent/100)
per_mount=per_year/12
all=dep_sum+(per_mount*srok)
print(all)
