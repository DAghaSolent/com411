
class Inhabitant:

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
    self.name = name
    self.age = 0
    self.energy = Inhabitant.MAX_ENERGY

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

