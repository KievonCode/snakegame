import pygame
import time
import random

#Initialize Pygame
pygame.init()

#colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

#Screen dimensions
width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#Background color
background_color = black
snake_block = 20
snake_draw_block = 20
snake_position = [500, 500]

#Initial snake body
snake_body = [[500, 500],
              [478, 500],
              [456, 500],
              [434, 500]]

snake_speed = 15
direction = 'LEFT'
running = True
fps = pygame.time.Clock()
score = 0
#Fruit position
fruit_position = [
    random.randrange(0, width // snake_block) * snake_block,
    random.randrange(0, height // snake_block) * snake_block
]
fruit_spawned = True

def die(score):
    #Create a font object for the game-over message
    my_font = pygame.font.SysFont('arial', 56)

    #Create a text surface for the game-over message
    game_over_surface = my_font.render('YOU SUCK', True, red)
    game_over_rect = game_over_surface.get_rect()

    #Center the gameover text on the screen
    game_over_rect.center = (width / 2, height / 2 - 50)

    #create a font object for the score
    score_font = pygame.font.SysFont('arial', 40)

    #Create a text surface for the score
    score_surface = score_font.render(f'Your score was only {score}.', True, white)
    score_rect = score_surface.get_rect()

    #Center the score text below the game-over message
    score_rect.center = (width / 2, height / 2 + 20)

    #Fill the screen with the background color
    screen.fill(background_color)

    #Draw the game-over message and score
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(score_surface, score_rect)

    #Update the display
    pygame.display.flip()
    time.sleep(2)

    pygame.quit()
    quit()



def scoring(score, color, font, size):
    #Create a font object
    score_font = pygame.font.SysFont(font, size)

    #Create a text surface
    score_surface = score_font.render('Score: ' + str(score), True, color)

    #Draw the score at the top-left corner of the screen
    screen.blit(score_surface, (10, 10))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    #Move the snake
    if direction == 'RIGHT':
        snake_position[0] += snake_block
    if direction == 'LEFT':
        snake_position[0] -= snake_block
    if direction == 'UP':
        snake_position[1] -= snake_block
    if direction == 'DOWN':
        snake_position[1] += snake_block

    #Update snake body
    snake_body.insert(0, list(snake_position))  # Add new head

    #Check if the snake eats the fruit
    if snake_position == fruit_position:
        fruit_spawned = False
        score += 1
    else:
        snake_body.pop()  #Remove tail to keep length constant if no fruit eaten

    #Spawn a new fruit if needed
    if not fruit_spawned:
        fruit_position = [
            random.randrange(0, width // snake_block) * snake_block,
            random.randrange(0, height // snake_block) * snake_block
        ]
        fruit_spawned = True

    #Fill background
    screen.fill(background_color)
    scoring(score, white, 'arial', 30)
    #Draw the fruit
    #pygame.draw.circle(screen, red, pygame.Rect(fruit_position[0], fruit_position[1], snake_draw_block, snake_draw_block))
    pygame.draw.circle(screen, red, (fruit_position[0] + snake_draw_block // 2, fruit_position[1] + snake_draw_block // 2), snake_draw_block // 2)

    #Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0] + 1, pos[1] + 1, snake_draw_block, snake_draw_block))

    #Update display and control speed
    pygame.display.flip()
    fps.tick(snake_speed)

    #Check if the snake exits the screen
    if snake_position[0] < 0 or snake_position[0] >= width:
        die(score)
    if snake_position[1] < 0 or snake_position[1] >= height:
        die(score)

    #check if the snake hits itself
    if snake_position in snake_body[1:]:
        die(score)

    

pygame.quit()
