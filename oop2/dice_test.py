#!/usr/bin/python3

# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def main():

    # create two cheater objects
    Mike = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    Glenn = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6

    # both players take turns
    Mike.roll()
    Glenn.roll()

    # both players use their cheat methods
    Mike.cheat()
    Glenn.cheat()

    print(f"Mike rolled {Mike.get_dice()}")
    print(f"Glenn rolled {Glenn.get_dice()}")

    if sum(Mike.get_dice()) == sum(Glenn.get_dice()):
        print("Draw!")

    elif sum(Mike.get_dice()) > sum(Glenn.get_dice()):
        print("Mike wins!")

    else:
        print("Glenn wins!")

if __name__ == "__main__":
    main()

