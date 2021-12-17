#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Creating a simple dice program utilizing classes."""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

def main():
    """called at run time"""

    ## create our player objects
    Mike = Player()
    Glenn = Player()

    Mike.roll()
    Glenn.roll()

    print(f"Mike rolled {Mike.get_dice()}")
    print(f"Glenn rolled {Glenn.get_dice()}")

    # determine which player won
    if sum(Mike.get_dice()) == sum(Glenn.get_dice()):
        print("Draw!")
    elif sum(Mike.get_dice()) > sum(Glenn.get_dice()):
        print("Mike wins!")
    else:
        print("Glenn wins!")


if __name__ == "__main__":
    main()

