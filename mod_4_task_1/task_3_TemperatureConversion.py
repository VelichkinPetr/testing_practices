

def check_correct_choice(choice: int) -> int:

    while choice not in [1,2]:
        choice = int(input('>>>'))

    return choice


def input_choice() -> int:

    print("Выберите опцию:")
    print("1. Конвертировать Цельсий в Фаренгейт")
    print("2. Конвертировать Фаренгейт в Цельсий")
    choice = int(input('>>>'))
    choice = check_correct_choice(choice)

    return choice


def input_temperature(choice: int) -> float:

    if choice == 1:
        temperature = float(input("Введите температуру в градусах Цельсия: "))

    elif choice == 2:
        temperature = float(input("Введите температуру в градусах Фаренгейта: "))

    return temperature


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def output_data(choice: int) -> float:

    if choice == 1:
        temperature = celsius_to_fahrenheit(input_temperature(choice))
        print(f"Температура в градусах Фаренгейта: {temperature:.2f}")

    elif choice == 2:
        temperature = fahrenheit_to_celsius(input_temperature(choice))
        print(f"Температура в градусах Цельсия: {temperature:.2f}")

    return temperature


def main() -> float:

    choice = input_choice()

    return output_data(choice)


if __name__ == "__main__":
    main()