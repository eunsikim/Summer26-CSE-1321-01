counter = 0

while True:
	if counter == 6:
		move(East)
		counter = 0
	else:
		move(North)
		counter += 1