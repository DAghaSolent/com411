from human import Human
from robot import Robot
from inhabitant import Inhabitant

if (__name__ == "__main__"):
  inhabitant = Inhabitant()

  danny = Human()
  danny.display()

  bender = Robot()
  bender.display()
