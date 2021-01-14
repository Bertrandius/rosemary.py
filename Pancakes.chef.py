# Chef Rosemary - Exercise 6: Pancakes

#Preamble - Importing Objects from libs
from kitchen import Rosemary
from kitchen.utensils import Bowl, Pan, Plate
from kitchen.ingredients import Flour, Egg, Salt, Milk, Butter

# Preparing our ingredients before we get to it
flour = Flour.take(grams = 250)
salt = Salt.take('dash')
eggs = Egg.take(2)
milk = Milk.take(ml = 500)

# Preparing our bowl, pan, and plate
bowl = Bowl.use(name = 'pancake batter')
pan = Pan.use(name = 'pancakes')
plate = Plate.use()

# Crack some eggs and put them into our bowl
for egg in eggs:
    egg.crack()
    bowl.add(egg)
bowl.mix() # Mixing them (until frothy?)

# Adding a pinch of salt to the bowl, and then mixing in our flour, 50g at a time.
bowl.add(Salt.take('dash'))
for i in range(5):
    bowl.add(flour.take('1/5'))
    bowl.mix()

# Mixing in milk, 250 ml at a time.
for i in range(2):
    bowl.add(milk.take('1/2'))
    bowl.mix()

# Cooking Pancakes
for i in range(8):
    pan.add(Butter.take('slice'))
    pan.add(bowl.take(portion='1/8'))
    for i in range(4):
        pan.cook(minutes = 0.5)
        pan.flip()
    pancake = pan.take()
    plate.add(pancake)

# Rosemary serves up the pancakes. Bone ape the teeth!
Rosemary.serve(plate)