class Animal:
    feed = 'Не покормлен'

    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed_1(self):
        self.feed = 'Покормлен'

    def __add__(self, other):

        return self.weight + other.weight


class Birds(Animal):
    collect = 'Не собраны'

    def collect_eggs(self):
        self.collect = 'Собраны'

class Dairy_cattle(Animal):
    milk = 'Не подоена'

    def milk_1(self):
        self.milk = 'Подоена'


class Wool(Animal):
    cut = 'Не подстрижена'

    def trim(self):
      self.cut = 'Подстрижена'

goose_1 = Birds('Серый', 12, 'гагага')
goose_2 = Birds('Белый', 8, 'гагага')
duck = Birds('Кряква', 3, 'кряяя')
chicken_1 = Birds('Ко-Ко', 3.1, 'кококо')
chicken_2 = Birds('Кукареку', 2.5, 'кококо')
cow = Dairy_cattle('Манька', 512, 'мууу')
goat_1 = Dairy_cattle('Рога', 50, 'меее')
goat_2 = Dairy_cattle('Копыта', 45, 'меее')
sheep_1 = Wool('Барашек', 90, 'беее')
sheep_2 = Wool('Кудрявый', 92, 'беее')

goose_1.feed_1()
cow.milk_1()
sheep_2.trim()


goose_1+goose_2