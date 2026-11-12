a=int(input('Введите число: '))
while True:
    k=0
    for i in range(1,a+1):
        if i*i==a:
            k=k+1
    if k==1:
        print('Полный квадрат')
        break
    else:
        a=int(input('Число не является полным квадратом. Введите новое: '))

