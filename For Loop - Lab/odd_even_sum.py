n=int(input())
even=0
odd=0
for num in range(1,n+1):
    numbers=int(input())
    if num % 2 == 0:
        even += numbers
    else:
        odd+=numbers
diff=even-odd
if odd == even :
    print('Yes')
    print(f'Sum = {even}')
else:
    print('No')
    print(f'Diff = {abs(diff)}')