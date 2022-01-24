from inhabitant import Inhabitant

class Robot(Inhabitant):
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0, energy=MAX_ENERGY):
        super(Robot, self).__init__(name, age, energy)

    def __repr__(self):
        return f"robot(name={self.name}, age={self.age})"

    def __str__(self):
        return f"{self.name} is {self.age} years old."

