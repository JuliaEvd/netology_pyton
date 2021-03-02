class Animals:
    sound = ""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self, food):
        self.weight = food + self.weight

    def make_sound(self):
        print(f"{self.name} издает звук {self.sound}")


class MilkGiving(Animals):
    def give_milk(self, milk):
        milk = self.weight // 10
        return f"Она дала {milk} литров молока"


class WoolGiving(Animals):
    def give_wool(self, wool):
        wool = self.weight // 10
        return f"Она дала {wool} граммов шерсти"


class EggGiving(Animals):
    def give_eggs(self, eggs):
        eggs = self.weight // 2
        return f"Она дала {eggs} яиц"


class Geese(Animals):
    sound = "gagaga"


class Cow(Animals):
    sound = "moooo"


class Sheep(Animals):
    sound = "beeee"


class Goat(Animals):
    sound = "maaaa"


class Duck(Animals):
    sound = "krya"


class Chicken(Animals):
    sound = "kokoko"


farm = []


def get_farm():
    farm.append(Geese("Белый", 5))
    farm.append(Geese("Серый", 6))
    farm.append(Cow("Манька", 300))
    farm.append(Sheep("Барашек", 78))
    farm.append(Sheep("Кудрявый", 90))
    farm.append(Chicken("Ко-ко", 3))
    farm.append(Chicken("Кукареку", 1))
    farm.append(Goat("Рога", 70))
    farm.append(Goat("Копыта", 58))
    farm.append(Duck("Кряква", 2))


def sounds():
    for all_animals in farm:
        all_animals.make_sound()


def commands():
    while True:
        command = input("Введите команду ")
        if command == "s":
            sounds()


get_farm()
commands()
sounds()
