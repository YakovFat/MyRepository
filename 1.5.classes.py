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

paddock = []
paddock.append(goose_1)
paddock.append(goose_2)
paddock.append(duck)
paddock.append(chicken_1)
paddock.append(chicken_2)
paddock.append(cow)
paddock.append(goat_1)
paddock.append(goat_2)
paddock.append(sheep_1)
paddock.append(sheep_2)

tmp = 0
for animal in paddock:
    tmp += animal.weight
print("Общий вес животных:", tmp)

maximum = 0
max_name = 0
for animal in paddock:
    if animal.weight >= maximum:
        maximum = animal.weight
        max_name = animal.name
print("Общий вес животных:", max_name)
