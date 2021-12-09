age=int(input('Enter Age: '))

while 0<=age<=120:
    if 0<=age<=18:
        print('child')

    elif 19<=age<=60:
        print('adult')

    else:
        print('senior')
    age = int(input('Enter Age: '))
