class User:
    count = 0

    def __init__(self, name: str, age:float or int):

        if not isinstance(name,str): raise TypeError
        if not isinstance(age, (float,int)): raise TypeError

        if len(name.strip()) == 0: raise ValueError
        if age < 1 or age > 100: raise ValueError

        self.__name = name
        self.__age = age
        User.count += 1

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> float or int:
        return self.__age

    def up_age(self, delta: float or int) -> float or int:

        if not isinstance(delta, (float, int)): raise TypeError
        if self.__age + abs(delta) > 100: raise ValueError

        self.__age += abs(delta)
        return self.get_age()

