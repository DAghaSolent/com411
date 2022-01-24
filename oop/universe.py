from planet import Planet
from human import Human
from robot import Robot
import matplotlib.pyplot as plt
import random


class Universe:
    def __init__(self):
        self.planets = []


    def generate(self):
        p = Planet()
        self.planets.append(p)
        random_number = random.randint(1, 10)
        for _ in range(random_number):
            h = Human()
            r = Robot()
            p.add_human(h)
            p.add_robot(r)

    def show_population(self):
        for planet in self.planets:
            humans = planet.inhabitants['humans']
            robots = planet.inhabitants['robots']
            humans_length = len(humans)
            robots_length = len(robots)
            labels = "Robots", "Humans"
            explode = (0, 0.1)
            plt.pie([humans_length, robots_length], labels=labels,explode=explode)
            plt.show()
            break






if(__name__ == "__main__"):
    universe = Universe()
    universe.generate()
    universe.show_population()













