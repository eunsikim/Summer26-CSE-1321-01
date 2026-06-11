# Create a program that moves a drone across a 6x6 tile map
# in an "S".
# The drone starts at the lower left corner tile of the map.
# The drone should start by moving north.
# The drone should cover the map like this:
# 	NORTH (to the edge) -> EAST (1 tile) -> SOUTH (to the edge) and so on.
# To move the drone a single tile, you have to use the `move()` function.
# Inside the function, you have to specify a cardinal direction:
#	North, South, East, or West

counter = 0

while True:
	if counter == 6:
		move(East)
		counter = 0
	else:
		move(North)
		counter += 1