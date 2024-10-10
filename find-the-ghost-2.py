import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRID_SIZE = 5
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ghost Hunt Game")

# Font setup
font = pygame.font.Font(None, 36)

# Game variables
grid = [["O" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
ghost_row = random.randint(0, GRID_SIZE - 1)
ghost_col = random.randint(0, GRID_SIZE - 1)
attempts = 5
game_over = False
ghost_found = False

def draw_grid():
    """Draws the 5x5 grid and the guesses."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)
            
            # Draw X for missed guesses
            if grid[row][col] == "X":
                pygame.draw.line(screen, RED, (col * CELL_SIZE, row * CELL_SIZE), 
                                 ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), 3)
                pygame.draw.line(screen, RED, ((col + 1) * CELL_SIZE, row * CELL_SIZE), 
                                 (col * CELL_SIZE, (row + 1) * CELL_SIZE), 3)
            
            # Draw G for the ghost
            if game_over and row == ghost_row and col == ghost_col:
                pygame.draw.circle(screen, GREEN, 
                                   (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 
                                   CELL_SIZE // 3)

def handle_click(pos):
    """Handles player's clicks for guesses."""
    global attempts, game_over, ghost_found
    
    if not game_over:
        col = pos[0] // CELL_SIZE
        row = pos[1] // CELL_SIZE
        
        if row < GRID_SIZE and col < GRID_SIZE:
            if grid[row][col] == "O":  # Only allow guesses on unmarked spots
                attempts -= 1
                if row == ghost_row and col == ghost_col:
                    ghost_found = True
                    game_over = True
                    grid[row][col] = "G"
                else:
                    grid[row][col] = "X"
                
                if attempts == 0 and not ghost_found:
                    game_over = True

def display_message(message):
    """Displays a message in the center of the screen."""
    text = font.render(message, True, RED)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

# Game loop
running = True
while running:
    screen.fill(BLUE)
    
    # Draw the grid
    draw_grid()
    
    # Check for win/loss and display appropriate message
    if game_over:
        if ghost_found:
            display_message("You found the ghost!")
        else:
            display_message(f"Out of attempts! Ghost was at ({ghost_row}, {ghost_col})")
    
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            handle_click(pygame.mouse.get_pos())
    
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
