

#### Now to run the game

# Now we will create the code that uses these objects in a separate file. 
# Create this bunco_single_test.py code 
# and make sure you save it in the same directory as bunco_module.py.

from bunco_module import Player
from bunco_module import Cheat_Swapper
from bunco_module import Cheat_Loaded_Dice

# create the instances of the children
cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()

# roll the dice
cheater1.roll()
cheater2.roll()

# now cheat
cheater1.cheat()
cheater2.cheat()

# and see who wins
print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
  print("Draw!")

elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
  print("Cheater 1 wins!")

else:
  print("Cheater 2 wins!")
