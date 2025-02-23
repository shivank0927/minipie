import copy
import random
import sys
import time


WIDTH = 79
HEIGHT = 20

ALIVE = '.' # alive and dead cells
DEAD = '1' 

# the cells, putting them in (x, y) tuple depending upon random lib.

nextCells = {}
# adding random dead / alive cells 
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True:
    
    print("\n" * 50)
    cells = copy.deepcopy(nextCells) # create deep copy of object

    for y in range(HEIGHT):
        for x in range(WIDTH):
            pass