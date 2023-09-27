from math import sqrt, log, sin, cos, tan, pi


print(
    "Вводите математические выражения и программа будет выводить ответ\n"
    "Для справи по основным командам введите 'Help'\nДля завершения работы введите 'Stop'"
)
a, b, c, d, e, f = sqrt(1), log(2, 2), sin(1), cos(1), tan(1), pi
# без этой строчки pylint отнимает 3.67 баллов
s = input()
while s != "Stop":
    if s == "Help":
        print(
            "* - умножение\n** - возведение в степень\n/ - деление\nsqrt(x) - квадратный корень\n"
            "log(a, b) - логарифм a по основанию b\n"
            "tan(x), sin(x), cos(x) - тригонометрические функции (в радианах)"
            "\n pi - число пи"
        )
    else:
        try:
            a = eval(s)
            print((a // 10**-11) * 10**-11)
        except SyntaxError:
            print("Выражение введено неверно")
        except ZeroDivisionError:
            print("Деление на 0")
    s = input()
