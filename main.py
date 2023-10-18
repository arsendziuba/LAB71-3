# Importing the Building class from Lab 7_1_2
from lab_7_1_2 import Building

# Creating two new Building objects
yellow_bricks = Building("Bricks", "Yellow", 200)
red_planks = Building("Planks", "Red", 10)

# Printing the initial state
print(f"{yellow_bricks.material} in {yellow_bricks.color}: {yellow_bricks.number} ({yellow_bricks.storage_place()})")
print(f"{red_planks.material} in {red_planks.color}: {red_planks.number} ({red_planks.storage_place()})")

# Adding 1 brick and removing 2 planks
yellow_bricks.plus(1)
red_planks.minus(2)

# Printing the updated state
print(f"{yellow_bricks.material} in {yellow_bricks.color}: {yellow_bricks.number} ({yellow_bricks.storage_place()})")
print(f"{red_planks.material} in {red_planks.color}: {red_planks.number} ({red_planks.storage_place()})")
