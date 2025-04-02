
from random import randint
x = randint(1, 6)

#creating a class with an attribute called sides and a method called roll_dice()
class Die():
    #initializing the class for the Die, including the attibute sides.
    def __init__(self, sides=6):
        self.sides = sides

    #createing the method: roll_dice()
    def roll_dice(self):
        return randint(1, self.sides)

#Using a 6 sided die, get results for rolling 10 times.
D6 = Die()

results = []
for number_rolls in range(10):
    result = D6.roll_dice()
    results.append(result)

# show what die was rolled and how many times
print("6-sided die rolled 10 time...")
print(results)
