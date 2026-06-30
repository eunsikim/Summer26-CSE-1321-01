# Create a function called `run` that takes in two variables.
# These two variables will represent the width and height of the map.
# Within the function, move the drone throughout the map.
# While moving through the map, the drone should plant Pumpkins, Bushes, and Carrots.
# The drone should plant these plants to create "columns" of Pumpkins, Bushes, and Carrots.
# The order of the "column" should be Pumpkin, Bush, Carrot, Pumpkin, Bush, Carrot, Pumpkin...
# The drone should stop after traversing each single tile (No infinite loop)

# The Farmer Was Replaced hints:
# To move the drone, the game uses the "move()" function. This function takes as argument: North, South, East, or West
# These arguments dictate which tile the drone will move into.
#
# To make the drone plant something, the game uses the "plant()" function. This function takes as argument:
# Entities.Pumpkin, Entities.Bush, or Entities.Carrot
# This function call will plant the designated plant under the drone.
#
# For Pumpkins and Carrots, the soil must be tilled. Before you call the "plant()" function, you must call the function "till()"
# this function does not take any arguments and it will just till the soil under the drone.

def run(width, height):
    # Start Here


