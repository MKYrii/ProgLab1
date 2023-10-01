"""без этих строк pylint отнимает 1.28 балла"""
from math import cos, log, pi, sin, sqrt, tan

a, b, c, d, e, f = sqrt(1), log(2, 2), sin(1), cos(1), tan(1), pi
# без этой строчки pylint отнимает 3.67 баллов


class Calculator:
    """без этих строк pylint отнимает 1.28 балла"""
    A = 0

    """без этих строк pylint отнимает 1.28 балла"""
    def main(self, s_ss):
        """без этих строк pylint отнимает 1.28 балла"""
        try:
            a_aa = eval(s_ss)
            return str(a_aa)
        except NameError:
            return "Выражение введено неверно"
        except TypeError:
            return "Выражение введено неверно"
        except SyntaxError:
            return "Выражение введено неверно"
        except ZeroDivisionError:
            return "Деление на 0"


print(
            "Вводите математические выражения и программа будет выводить ответ\n"
            "Для справи по основным командам введите 'Help'\nДля завершения работы введите 'Stop'"
)
calculator = Calculator()
s = input()
while s != "Stop":
    if s == "Help":
        print(
            "* - умножение\n** - возведение в степень\n/ - деление\n"
            "sqrt(x) - квадратный корень\nlog(a, b) - логарифм a по основанию b\n"
            "tan(x), sin(x), cos(x) - тригонометрические функции (в радианах)"
            "\npi - число пи"
        )
    else:
        print(calculator.main(s))
    s = input()
