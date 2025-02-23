import copy
import random
import sys
import time

try:
    width = int(input("Enter the width of cell for simulation\n>>> "))
    height = int(input("Enter the height of cell for simulation\n>>> "))
    cell = str(input("Enter a character to represent alive cell ( dead cell will be blank! )\n>>> "))
    
except ValueError:
    print("Wrong value entered")

alive = f'{cell}' # alive and dead cells
dead = ' '

# adding random dead / alive cells
def initialize(width, height, alive, dead):
    grid = {}
    for x in range(width):
        for y in range(height):
            if random.randint(0, 1) == 0:
                grid[(x, y)] = alive
            else:
                grid[(x, y)] = dead
    return grid

# display the grid
def display(grid, width, height, simulation):
    print("\n" * 50)
    for y in range(height):
        for x in range(width):
            print(grid[(x, y)], end='')
        print()
    print(f"Simulation: {simulation}")
    print("press Ctrl + C to exit.")

# count number of living neighbours
def count_neighbors(grid, x, y, width, height, alive):
    neighbors = [
        ((x - 1) % width, (y - 1) % height),
        (x, (y - 1) % height),
        ((x + 1) % width, (y - 1) % height),
        ((x - 1) % width, y),
        ((x + 1) % width, y),
        ((x - 1) % width, (y + 1) % height),
        (x, (y + 1) % height),
        ((x + 1) % width, (y + 1) % height),
    ] # initializing every possible cell pos which is either alive or dead
    count = 0
    for nx, ny in neighbors:
        if grid[(nx, ny)] == alive:
            count += 1
    return count

# setup of cells
def update(grid, width, height, alive, dead):
    new_grid = copy.deepcopy(grid)
    for x in range(width):
        for y in range(height):
            neighbors = count_neighbors(grid, x, y, width, height, alive)
            if grid[(x, y)] == alive and (neighbors == 2 or neighbors == 3):
                new_grid[(x, y)] = alive
            elif grid[(x, y)] == dead and neighbors == 3:
                new_grid[(x, y)] = alive
            else:
                new_grid[(x, y)] = dead
    return new_grid

def main():
    grid = initialize(width, height, alive, dead)
    simulation = 1
    
    while True:
        display(grid, width, height, simulation)
        grid = update(grid, width, height, alive, dead)
        simulation += 1
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            sys.exit("stopped!")

if __name__ == "__main__":
    main()