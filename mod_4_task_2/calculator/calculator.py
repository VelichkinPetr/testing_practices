class Calculator:

    def add(self, value_left, value_right) -> float:

        if not isinstance(value_left, (int, float)): raise TypeError
        if not isinstance(value_right, (int, float)): raise TypeError

        return value_left + value_right

    def subtract(self, value_left, value_right) -> float:
        return value_left - value_right

    def multiply(self, value_left, value_right) -> float:

        if not isinstance(value_left, (int,float)): raise TypeError
        if not isinstance(value_right, (int,float)): raise TypeError

        return value_left * value_right

    def divide(self, value_left, value_right) -> float:
        return value_left / value_right