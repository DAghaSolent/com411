class Robot:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = Robot.MAX_ENERGY

    def __repr__(self):
        return f"robot(name={self.name}, age={self.age})"

    def __str__(self):
        return f"Robot {self.name} is {self.age} years old."

    def display(self):
        print(f"I am {self.name}")

if (__name__ == "__main__"):
    bender = Robot()
    print(bender)
    print()
    print(repr(bender))