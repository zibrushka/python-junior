"""
Что будет выведено после выполнения кода? Почему?
"""

"""
Ответ:
В результате выполнения кода будет выведено дважды число 3.
первый раз в результате выполнения вложенной функции printer
nonlocal позволяет объявлять переменную ближайшей области видимости, 
а нашем случае это родитель вложенной функции printer - функция print_msg, 
таким образом мы меняем переменную функции print_msg - number, переданную в качестве аргумента.

второй раз как результат исполнения функции print_msg, 
сначала вложенной функцией меняется значение переменной, затем выводится сама переменная, 
поэтому выводится 3 а не 9
"""

def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)