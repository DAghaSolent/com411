class Human:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY


    def __repr__(self):
        return f"human(name={self.name}, age={self.age})"


    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def grow(self):
        self.age += 1

    def eat(self, amount):
        if self.energy < 100:
            self.energy += amount
        else:
            print("You have maxed out on your energy levels")

    def distance(self, distance):
        if self.energy > 0:
            self.energy -= distance
        else:
            print("Your energy is low. You must run the eat method to replenish your energy.")


    def display(self):
        print(f"I am {self.name}")


if(__name__ == "__main__"):
    danny = Human()
    print(danny)
    print()
    print(danny.distance(40))
    print(danny.energy)
    print()
    print(danny.eat(20))
    print()
    danny.display()

