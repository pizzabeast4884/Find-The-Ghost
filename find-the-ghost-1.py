import random

# Initialize a 5x5 grid
grid_size = 5
grid = [["O" for _ in range(grid_size)] for _ in range(grid_size)]

# Randomly select ghost position
ghost_row = random.randint(0, grid_size - 1)
ghost_col = random.randint(0, grid_size - 1)

# Allow the player 5 guesses
attempts = 5
for attempt in range(attempts):
    print(f"Attempt {attempt + 1} of {attempts}")
    
    # Display the current grid
    for row in grid:
        print(" ".join(row))
    
    # Get player's guess
    guess_row = int(input("Guess the row (0-4): "))
    guess_col = int(input("Guess the column (0-4): "))
    
    if guess_row == ghost_row and guess_col == ghost_col:
        print("You found the ghost!")
        grid[ghost_row][ghost_col] = "👻"  # Mark ghost position
        for row in grid:
            print(" ".join(row))  # Show the final grid with ghost
        break
    else:
        print("No ghost here! Keep looking.")
        grid[guess_row][guess_col] = "X"  # Mark this spot

else:
    print("You're out of attempts! The ghost was at:", ghost_row, ghost_col)
    grid[ghost_row][ghost_col] = "👻"  # Mark ghost position
    for row in grid:
        print(" ".join(row))  # Show the final grid with ghost
