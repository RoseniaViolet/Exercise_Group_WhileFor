n = input('Enter product price: ')
S = 0
while n != '':
    n = float(n) 
    n = input('Enter product price (press Enter to finish): ')
a = S % 5
if a < 2.5:
    print(f'Total product amount: {S}, when paying cash: {S - a}')
elif a >= 2.5: 
    print(f'Total product amount: {S}, when paying cash: {S + (5 - a)}')

    