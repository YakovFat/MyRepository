class Animal:
    feed = 'Не покормлен'
    voice = 'hi'
    name = 'name'
    weight = 0

    def name_1(self, name):
        self.name = name

    def weight_1(self, weight):
        self.weight = weight

    def feed_1(self):
        self.feed = 'Покормлен'


class Birds(Animal):
    collect = 'Не собраны'

    def collect_eggs(self):
        self.collect = 'Собраны'

class Dairy_cattle(Animal):
    pass

class Wool(Animal):
    pass

goose_1 = Birds()
goose_2 = Birds()
duck = Birds()
chicken_1 = Birds()
chicken_2 = Birds()
cow = Dairy_cattle()
goat_1 = Dairy_cattle()
goat_2 = Dairy_cattle()
sheep_1 = Wool()
sheep_2 = Wool()

print(sheep_1.weight)


