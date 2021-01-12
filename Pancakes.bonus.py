# Chef Rosemary - Exercise 6: Pancakes

# Premable - Importing Objects from libs
from kitchen import Rosemary
from kitchen.utensils import Bowl, Pan, Plate
from kitchen.ingredients import Flour, Egg, Salt, Milk, Butter

def pancakes(number): # Specify number of pancakes

    # Preparing our ingredients before we get to it
    flour = Flour.take(grams = int((250/8)*number))
    if number < 16:
        salt = Salt.take('dash')
    else:
        salt = Salt.take(amount='generous dash')
    eggs = Egg.take(int((2/8)*number))
    milk = Milk.take(ml = int((500/8)*number))

    # Preparing our bowl, pan, and plate
    bowl = Bowl.use(name = 'pancake batter')
    pan = Pan.use(name = 'pancakes')
    plate = Plate.use()

    # Crack some eggs and put them into our bowl
    for egg in eggs:
        egg.crack()
        bowl.add(egg)
    bowl.mix() # Mixing them (until frothy?)

    # Adding a pinch of salt to the bowl, and then mixing in our flour, 50g of total content at a time.
    bowl.add(salt)
    #flour.amount
    for i in range(5):
        bowl.add(flour.take('1/5'))
        bowl.mix()

    # Mixing in milk, 250 ml at a time.
    for i in range(2):
        bowl.add(milk.take('1/2'))
        bowl.mix()

    # Cooking Pancakes
    for i in range(number):
        pan.add(Butter.take('slice'))
        pan.add(bowl.take(portion=f'1/{number}'))
        for i in range(4):
            pan.cook(minutes = 0.5)
            pan.flip()
        pancake = pan.take()
        plate.add(pancake)

    return plate

plate = pancakes(14)

# Rosemary serves up the pancakes. Bon appetit!
Rosemary.serve(plate)