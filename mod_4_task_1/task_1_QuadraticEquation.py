import math


def check_is_zero(a: float) -> float:

    while a == 0:
        print("Коэффициент a не может быть равен нулю для квадратного уравнения.")
        a = float(input('a: '))

    return a


def input_data() -> tuple[float]:

    print("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0")
    a = float(input('a: '))
    a = check_is_zero(a)
    b = float(input('b: '))
    c = float(input('c: '))

    return a,b,c


def calculating_roots(a:float ,b: float,c: float) -> tuple[float] or float or None:

    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1,root2

    elif discriminant == 0:
        root = -b / (2 * a)
        return root

    else:
        return None


def output_data(roots: tuple[float] or float or None) -> None:

    if roots is None:
        print("У уравнения нет действительных корней")

    elif isinstance(roots,tuple) and len(roots) == 2:
        print(f"Корни уравнения: {roots[0]:.2f} и {roots[1]:.2f}")

    elif isinstance(roots, float):
        print(f"Единственный корень уравнения: {roots:.2f}")


def main() -> tuple[float] or float or None:

    roots = calculating_roots(*input_data())
    output_data(roots)

    return roots


if __name__ == '__main__':
    main()