# Лабораторная работа №2. Разветвляющиеся вычислительные процессы
# Задание №2, вариант (рисунок) 2.
# Проверяется попадание точки (x, y) в серую область.
# Точки на границе области считаются попавшими.

def point_in_region(x, y, r):
    if r <= 0:
        raise ValueError("Радиус R должен быть больше нуля.")

    # Область 1: четверть круга в верхней левой части:
    # x^2 + y^2 <= R^2, x <= 0, y >= 0.
    in_quarter_circle = (
        x <= 0 and y >= 0 and x * x + y * y <= r * r
    )

    # Область 2: треугольник с вершинами (0, 0), (R, 0), (R/2, -R).
    # Его границы: y <= 0, y >= -2*x, y >= 2*x - 2*R.
    in_triangle = (
        y <= 0
        and y >= -2 * x
        and y >= 2 * x - 2 * r
        and 0 <= x <= r
    )

    return in_quarter_circle or in_triangle


def main():
    print("Лабораторная работа №2, задание 2, вариант 2")
    print("Введите координаты точки X, Y и радиус R.")
    try:
        x = float(input("X = "))
        y = float(input("Y = "))
        r = float(input("R = "))
        if r <= 0:
            print("Ошибка: радиус R должен быть больше нуля.")
            return
    except ValueError:
        print("Ошибка: необходимо вводить числа.")
        return

    if point_in_region(x, y, r):
        print("Попадает")
    else:
        print("Не попадает")


if __name__ == "__main__":
    main()
