from decimal import *

def is_that_number(mes):               # Позволяет ввести с коносоли вещественное число (кроме 0), возвращая
  print(mes)                           # пользователя ко вводу каждый раз, если ввод не корректен
  val = input('=>  ')
  try:
    if int(val) == 0:
        raise Exception("\033[1;31mЧисло не должно быть равно 0\033[0m")
    return int(val)    
  except ValueError:
    print('\033[1;31mЭто не число!\033[0m')  
    return is_that_number(mes)
  except Exception as e:
    print(e)
    return is_that_number(mes)

print('\n'*3)
print('\t\tЗадача 2')
print('*'*56)
print('  Вычислить число c заданной точностью d')    
num1 = Decimal(is_that_number('Введите числитель '))
num2 = Decimal(is_that_number('Введите знаменатель '))
d = is_that_number('Укажите точность – количество знаков после запятой')
print(f'{num1}/{num2} = ', + round(num1 / num2, d))
print('*'*56)
print('\n'*3)