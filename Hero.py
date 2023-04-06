class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.named = name
        self.nicknamed = nickname
        self.superpowers = superpower
        self.health_point = health_points
        self.catchphrases = catchphrase

    def name(self):
        return (self. named)

    def health_points(self):
        return (self.health_point*2)

    def __str__(self):
        return f'{self.nicknamed}, {self.superpowers}, {self.health_point}'

    def __len__(self):
        return len(self.catchphrases)


spider = SuperHero ('Питер', 'Человек-паук', 'Живучесть', 500, 'Сосед')
Hero = SuperHero ('Питер', 'Человек-паук', 'Живучесть', 500, 'Сосед')

#spider.name()

#spider.health_points()

#print(spider)

#print(len(spider))

#print(Hero.name())
#print(Hero.health_points())
#print(Hero)
#print(len(Hero))

