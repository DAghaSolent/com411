from planet import Planet
from human import Human
import random


class Universe:
    def __init__(self):
        self.planets = []

    def generate(self,):
        p = Planet()
        self.planets.append(p)
        random_number = random.randint(1, 10)
        for _ in random_number:
            h = Human()
            p.add_human(h)

if(__name__ == "__main__"):
    print(p)













