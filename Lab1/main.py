# Лабораторная работа №1. Линейные программы
# Задание №2 из списка заданий к лабораторной работе №1
# Сравнение двух выражений для пяти тестовых значений alpha.

from math import sin, cos, pi, sqrt

def calculate(alpha):
    # Первое выражение
    z1 = cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha)

    # Второе выражение
    z2 = 2 * sqrt(2) * cos(alpha) * sin(pi / 4 + 2 * alpha)

    return z1, z2


def main():
    print("Лабораторная работа №1, задание 2")
    print("Угол alpha вводится в радианах.")
    try:
        alpha = float(input("Введите alpha: "))
    except ValueError:
        print("Ошибка: необходимо ввести число.")
        return

    z1, z2 = calculate(alpha)
    print(f"z1 = {z1:.6f}")
    print(f"z2 = {z2:.6f}")
    print(f"Разность |z1 - z2| = {abs(z1 - z2):.10f}")

    print("\nПроверка на пяти тестовых значениях:")
    print(f"{'alpha':>10} {'z1':>14} {'z2':>14} {'Совпадают':>12}")
    for test_alpha in [-1.0, -0.5, 0.0, 0.5, 1.0]:
        a, b = calculate(test_alpha)
        match = "Да" if math_isclose(a, b) else "Нет"
        print(f"{test_alpha:10.2f} {a:14.6f} {b:14.6f} {match:>12}")


def math_isclose(a, b):
    return abs(a - b) < 1e-9


if __name__ == "__main__":
    main()
