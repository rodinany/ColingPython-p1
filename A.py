class SpaceObject:
    def __init__(self, name=None):
        self.name = name

class Planet(SpaceObject):
    def __init__(self, name, population=None):
        super().__init__(name)
        self.population = population or 0

    def __str__(self):
        return f'Population of {self.name} = {self.population}'

class Animal:
    def __init__(self, name=None, planet=None):
        self.name = name
        self.planet = planet

    def come_into_being(self, planet):
        self.planet = planet
        self.planet.population += 1

class Cat(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().come_into_being(planet)
        self.fullness = 50
        self.mood = 20

    def eat(self):
        self.fulness += 10
        self.mood += 5

    def sleep(self):
        self.fullness -= 20
        self.mood += 10


class Dinosaur(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().come_into_being(planet)
        self.fullness = 50
        self.mood = 20

    def hunt(self):
        self.fulness -= 30
        self.mood += 10

    def eat(self):
        self.fulness += 40
        self.mood += 20


class Dog(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().come_into_being(planet)
        self.fullness = 50
        self.mood = 20

    def play(self):
        self.fulness -= 20
        self.mood += 20

    def eat(self):
        self.fulness += 20
        self.mood += 10

earth = Planet('Earth')

cats = [Cat('Wiskerson', earth),
        Cat('Simon', earth),
        Cat('Salem', earth),
]
dinosaurs = [Dinosaur('Rex', earth),
        Dinosaur('Pluto', earth),
]
dogs = [Dog('Goofy', earth)]

print(earth)
