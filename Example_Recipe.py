from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt

bowl = Bowl.use(name='batter')

# Add all the eggs to the batter and mix
for egg in Egg.take(6):
    egg.crack()
    bowl.add(egg)

bowl.mix()

Rosemary.taste(bowl)

plate = Plate.use(name='omelettes')

# Make two omelettes
for i in range(2):
    # Make a single omelette
    omelette_pan = Pan.use(name='omelette')
    omelette_pan.add(Butter.take('slice'))
    omelette_pan.add(bowl.take('1/2'))
    omelette_pan.add(Salt.take('dash'))
    omelette_pan.cook(minutes=2)
    plate.add(omelette_pan.take())

Rosemary.serve(plate)