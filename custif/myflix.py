#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'The car is going '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("How fast is the car moving in mph?"))

# if input value was higher or equal to 25
if connection >= 100:
    message = message + 'really fast.'
elif connection >= 50:
    message = message + 'the speed limit.'
elif connection >= 25:
    message = message + 'too slow.'
else:
    message = message + 'not fast enough.'
print(message)

