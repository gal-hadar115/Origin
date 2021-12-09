day=int(input('enter day: '))
month=int(input('enter month: '))
year=int(input('enter year: '))

if 1<=day<=31 and 1<month<=12 and 1950<=year<=2020:
    print(f'{day}/{month}/{year//10%10}{year%10}')
else:
    print('date not eligible')





