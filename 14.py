s=input('Введите число: ')
while True:
    d=int(s.isdigit())
    if d==0:
        s=input('Ошибка. Попробуйте еще раз. Введите число: ')
    if d==1:
        print('Введено целое число:',s)
        break
