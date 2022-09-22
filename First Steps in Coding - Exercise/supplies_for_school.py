pac_him=float(5.8)
pac_markeri=float(7.2)
perar_lit=float(1.2)
broi_pac_him=int(input())
broi_pac_markeri=int(input())
lit_preparat=int(input())
proc_namalenie=float(input())

pari_himikali=pac_him*broi_pac_him
pari_markeri=pac_markeri*broi_pac_markeri
pari_preparat=lit_preparat*perar_lit

obshto_pari=pari_preparat+pari_markeri+pari_himikali

nam_suma= obshto_pari*(proc_namalenie/100)
obshto_s_namalenie=obshto_pari-nam_suma
print(obshto_s_namalenie)