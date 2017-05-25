
#### Inheritence

	# Objects that inherit from a parent are defined using the same class keyword.
	# the name of the parent is placed inside parentheses of the child.
	# the child inherits all the variables and methods(functions) from the parent.
	# plue the child can have additional variables and methods.

## from : https://www.raspberrypi.org/magpi/class-python/
## and : https://www.raspberrypi.org/magpi/inheritance-python/

from random import randint

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6
    # finds last item in list and swaps it for a 6.

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice):
      if self.dice[i] < 6:
        self.dice[i] += 1
      i += 1
    # This method iterates through the dice in the list, 
    # checking whether each die is lower than six. 
    # If so, it increases its value by one






