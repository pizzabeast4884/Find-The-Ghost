import random

# Initialize a 5x5 grid
grid_size = 5
grid = [["0" for _ in range(grid_size)] for _ in range(grid_size)]

# Randomly select pumpkin position
pumpkin_row = random.randint(0, grid_size - 1)
pumpkin_col = random.randint(0, grid_size - 1)

# Allow the player 5 guesses
attempts = 10
for attempt in range(attempts):
    print(f"Attempt {attempt + 1} of {attempts}")
    
    # Display the current grid
    for row in grid:
        print(" ".join(row))
    
    # Get player's guess
    guess_row = int(input("Guess the row (1-5): "))-1
    guess_col = int(input("Guess the column (1-5): "))-1
    
    if guess_row == pumpkin_row and guess_col == pumpkin_col:
        print("You found the pumpkin!")
        grid[pumpkin_row][pumpkin_col] = "🎃"  # Mark pumpkin position
        for row in grid:
            print(" ".join(row))  # Show the final grid with pumpkin
        break
    else:
        print("No pumpkin here! Keep looking.")
        grid[guess_row][guess_col] = "X"  # Mark this spot

else:
    print("You're out of attempts! The pumpkin was at:", pumpkin_row, pumpkin_col)
    grid[pumpkin_row][pumpkin_col] = "🎃"  # Mark pumpkin position
    for row in grid:
        print(" ".join(row))  # Show the final grid with pumpkin
