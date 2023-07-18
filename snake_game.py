import pygame
import random
from snake import Snake

# Initialize the game
pygame.init()

# Set the initial width and height of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set the size of each snake segment
SNAKE_SEGMENT = 20

# Set the speed of the snake
SPEED = 10

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Snake Game')

# Define the main game loop
def game_loop():
    def check_for_event():
        # Check for key press to play again or quit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_loop()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

    global WINDOW_WIDTH, WINDOW_HEIGHT

    # flag used to control the game in case of failure
    game_over = False
    game_close = False

    # Create the snake
    snake_obj = Snake()
    snake_length = 1

    # Starting position of the snake
    x1 = WINDOW_WIDTH / 2
    y1 = WINDOW_HEIGHT / 2

    # Initial movement direction
    new_x1 = 0
    new_y1 = 0

    # Create the food at a random position
    food_x = round(random.randrange(0, WINDOW_WIDTH - SNAKE_SEGMENT) / SNAKE_SEGMENT) * SNAKE_SEGMENT
    food_y = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_SEGMENT) / SNAKE_SEGMENT) * SNAKE_SEGMENT

    # Main game loop
    while not game_over:
        while game_close:
            # Display game over message
            window.fill(BLACK)
            font_style = pygame.font.SysFont(None, 30)
            message = font_style.render("Game Over! Press C-Play Again or Q-Quit", True, GREEN)
            # The blit() function in Pygame is used 
            # to copy the pixels from one surface (source) onto another surface (destination). 
            # In this case, it is used to transfer the text message onto the game window.
            window.blit(message, [WINDOW_WIDTH / 4, WINDOW_HEIGHT / 3])
            # update window
            pygame.display.update()

            # Check for key press to play again or quit
            check_for_event()

        # Handle movement and boundary collisions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x1 = -SNAKE_SEGMENT
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = SNAKE_SEGMENT
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -SNAKE_SEGMENT
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = SNAKE_SEGMENT
                    new_x1 = 0

        # Update the snake's position
        x1 += new_x1
        y1 += new_y1

        # Check for boundary collisions
        if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
            game_close = True

        # Clear the game window
        window.fill(BLACK)

        # Draw the food
        pygame.draw.rect(window, RED, [food_x, food_y, SNAKE_SEGMENT, SNAKE_SEGMENT])

        # Update the snake's segments
        head_position = [x1, y1]
        snake_obj.add_new_position(position = head_position)

        # the logic is that at every iteration we add to the snake the new position 
        # and we delete the queue if no collision with food
        if len(snake_obj) > snake_length:
            snake_obj.snake_remove_queue()

        # Check for self-collision
        if snake_obj.is_intersecting():
            game_close = True

        # Draw the snake
        snake_obj.draw_snake(window, SNAKE_SEGMENT)

        # Update the game window
        pygame.display.update()

        # Check for food collision
        if x1 == food_x and y1 == food_y:
            # Generate new food position
            food_x = round(random.randrange(0, WINDOW_WIDTH - SNAKE_SEGMENT) / SNAKE_SEGMENT) * SNAKE_SEGMENT
            food_y = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_SEGMENT) / SNAKE_SEGMENT) * SNAKE_SEGMENT
            snake_length += 1

        # Set the snake's speed
        clock = pygame.time.Clock()
        clock.tick(SPEED)

        # Update the game window size if it's resized
        WINDOW_WIDTH, WINDOW_HEIGHT = window.get_size()

    # Quit the game
    pygame.quit()
    quit()

# Start the game loop
game_loop()
