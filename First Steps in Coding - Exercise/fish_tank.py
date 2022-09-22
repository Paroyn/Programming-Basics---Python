dulj=float(input())
shirochina=float(input())
vishochina=float(input())
procent=float(input())

obem=float(dulj*shirochina*vishochina)
obem_litri=float(obem*0.001)

proc_zaeto=float(obem_litri*(procent/100))

obshto=float(obem_litri-proc_zaeto)
print(obshto)