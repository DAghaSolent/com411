class Planet:

    def __init__(self):
        self.inhabitants = {
            'humans': [],
            'robots': []
            }


    def add_human(self, human):
        self.inhabitants['humans'].append(human)

    def remove_human(self, human):
        self.inhabitants['humans'].remove(human)

    def add_robot(self, robot):
        self.inhabitants['robots'].append(robot)

    def remove_robot(self, robot):
        self.inhabitants['robots'].remove(robot)

    def __repr__(self):
        return f"humans(humans={self.inhabitants['humans']},robots(robots={self.inhabitants['robots']}"

    def __str__(self):
        return f"{self.inhabitants['humans']} and {self.inhabitants['robots']}"


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
