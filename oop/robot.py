class Robot:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = Robot.MAX_ENERGY

    def __repr__(self):
        return f"robot(name={self.name}, age={self.age})"

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def display(self):
        print(f"I am {self.name}")

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

if (__name__ == "__main__"):
    bender = Robot()
    print(bender)
    print()
    print(bender.distance(40))
    print(bender.energy)
    print()
    print(bender.eat(20))
    print(bender.energy)
