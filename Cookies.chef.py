# Chef Rosemary - Exercise 7: Chocolate Chip Cookies

# Pre-preamble - Loading Concept of Time
import time

# Premable - Importing Necessary Stuff from libs (the pantry)
from kitchen import Rosemary
from kitchen.utensils import Bowl, Oven, BakingTray, Plate
from kitchen.ingredients import Butter, Sugar, Egg, Flour, BakingPowder, Salt, ChocolateChips

# Initializing Ingredients
butter = Butter.take(amount = 'part')
sugar = Sugar.take(grams=200)
eggs = Egg.take(2)
salt = Salt.take(amount='pinch')
flour = Flour.take(grams=300)
choc_chips = ChocolateChips.take(grams=200)
bpowder = BakingPowder.take(amount = 'some')

# Initializing Utensils
bowl = Bowl.use(name = 'batter')
oven = Oven.use()
baking_tray = BakingTray.use()
plate = Plate.use()

# Preheat Oven
oven.preheat(degrees=175)

# Mixing Butter w/ Sugar
bowl.add(butter)
for i in range(6):
    bowl.add(sugar.take('1/6'))
    bowl.mix()

# Mixing Batter w/ Eggs
for egg in eggs:
    egg.crack()
    bowl.add(egg)
    bowl.mix()

# Add a pinch of salt
bowl.add(salt)
bowl.mix()

# Add flour & chocolate chips
for i in range(6):
    bowl.add(flour.take('1/6'))
    bowl.add(choc_chips.take('1/6'))
    bowl.mix()

# Add Baking Powder
bowl.add(bpowder)

# Transfer Batter to Baking Tray
for i in range(20):
    baking_tray.add(bowl.take(portion='1/20'))

# Put Baking Tray in the Oven & Baking
oven.add(baking_tray)
oven.bake(minutes=10)

# Remove Tray from Oven and Place on Plate
baked_tray = oven.take()
plate.add(baked_tray.take())

# Wait for Cookies to Cool, and Then Serve!
time.sleep(5) # Waits 10 seconds for the cookies to cool.
Rosemary.serve(plate)