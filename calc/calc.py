print("Вас приветствует спортивный калькулятор")
print("Доступные операции (сложение) (вычитание) (умножение) (деление) (возведение в степень) (деление с остатком) ")
a = float(input("Введите очки: "))
b = float(input("Введите раунды: "))
operation = input("Введите знак операции (+,-,*,//,/,%,**,ВЫХОД)")
while True:
        if operation == "+":
            result = a + b
            print("Сумма:", a, "+", b, '=', result)
        elif operation == '-':
            result = a - b
            print("Разность:", a, '+', b, '=', result)
        elif operation == '*':
            result = a * b
            print('Умножение:', a, "*", b, '=', result)
        elif operation == '%':
            result = a % b
            print('Деление с остатком:', a, '%', b, '=', result)
        elif operation == '/':
            if b == 0:
                 print("Введите другое число")
                 result = "ошибка"
                 break
            else:
                result = a / b
            print('Деление на цело:', a, '/', b, '=', result)
        elif operation == '**':
            result = a ** b
            print('Возведение в с степень:', a, '**', b, '=', result)
        elif operation == 'ВЫХОД':
            print('Выход с калькулятора')
            break
