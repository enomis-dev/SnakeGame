import pygame

# Define the colors for the snake's body
snake_colors = [(0, 204, 102), (0, 255, 0), (51, 204, 51), (0, 153, 0)]

class Snake:
    # class that represents the snake object

    def __init__(self):
        self.head_position = [[0, 0]]
        self.snake = []
        self.add_new_position()
    
    def __len__(self):
        # return snake length
        return len(self.snake)
    
    def add_new_position(self, position = [0, 0]):
        # add position
        self.snake.append(position)

    def snake_remove_queue(self):
        # remve snake queue
        del self.snake[0]

    def draw_snake(self, window, segment_size):
        # Draw the snake
        for i, segment in enumerate(self.snake):
            pygame.draw.circle(window, snake_colors[i % len(snake_colors)], (int(segment[0]) + int(segment_size / 2), int(segment[1]) + int(segment_size / 2)), int(segment_size / 2))

    def is_intersecting(self):
        # is intersecting
        for segment in self.snake[:-1]:
            if segment == self.snake[-1]:
                return True
            