from inhabitant import Inhabitant

class Human(Inhabitant):
    MAX_ENERGY = 100

    def __init__(self, name="human", age=0, energy=MAX_ENERGY):
        super(Human, self).__init__(name, age, energy)


    def __repr__(self):
        return f"human(name={self.name}, age={self.age})"


    def __str__(self):
        return f"{self.name} is {self.age} years old."




