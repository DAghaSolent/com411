class Planet:
    def __init__(self):
        self.humans = []
        self.robots = []

    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self, human):
        self.humans.remove(human)

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        self.robots.remove(robot)

    def __repr__(self):
        return f"humans(humans={self.humans},robots(robots={self.robots}"

    def __str__(self):
        return f"{self.humans} and {self.robots}"


if(__name__ == "__main__"):
    planet = Planet()
    planet.add_human("Danny")
    print(planet)
    planet.add_human("Tanya")
    print(planet)
    planet.add_robot("Bender")
    print(planet)
    planet.add_human("Darren")
    print(planet)
    planet.add_robot("Clamps")
    print(planet)
    planet.remove_robot("Clamps")
    planet.remove_human("Darren")
    print()
    print()
    print(planet)