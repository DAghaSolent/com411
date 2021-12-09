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

    def display(self):
        print(f"I am {self.name}")

if(__name__ == "__main__"):
    danny = Human()
    print(danny)
    print()
    print(repr(danny))

