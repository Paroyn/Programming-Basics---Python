budged=float(input())
n=int(input())
m=int(input())
p=int(input())
n_cena=n*250
m_cena=float((n_cena*0.35)*m)
p_cena=float((n_cena*0.1)*p)
all_price=float(n_cena+m_cena+p_cena)
if n>m:
    all_price=float(all_price-(all_price*0.15))
if budged>=all_price:
    leftover=budged-all_price
    print(f'You have {leftover:.2f} leva left!')
else:
    leftover=abs(budged-all_price)
    print(f'Not enough money! You need {leftover:.2f} leva more!')