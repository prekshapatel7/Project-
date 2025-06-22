
import pygame
import time
import random

# Initialize pygame
pygame.init()

# Window size
window_x = 720
window_y = 480

# Game window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game by Preksha')

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# FPS controller
fps = pygame.time.Clock()

# Snake default position and body
snake_pos = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50]]

# Food position
food_pos = [random.randrange(1, (window_x//10)) * 10,
            random.randrange(1, (window_y//10)) * 10]
food_spawn = True

# Snake direction
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

# Display Score
def show_score():
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render('Score : ' + str(score), True, white)
    game_window.blit(score_surface, (10, 10))

# Game Over
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render('Your Score is : ' + str(score), True, red)
    game_window.blit(game_over_surface, (window_x//4, window_y//3))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main Logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    
    direction = change_to

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
        
    if not food_spawn:
        food_pos = [random.randrange(1, (window_x//10)) * 10,
                    random.randrange(1, (window_y//10)) * 10]
    food_spawn = True

    # Background and drawing
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(game_window, blue, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Game Over conditions
    if (snake_pos[0] < 0 or snake_pos[0] > window_x - 10 or
        snake_pos[1] < 0 or snake_pos[1] > window_y - 10):
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()
    
    show_score()
    pygame.display.update()
    fps.tick(15)
