import pygame
import random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Cobrinha')

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((0,255,255))

my_direction = LEFT

clock = pygame.time.Clock()
score = 0

game_over = False

bg = pygame.image.load('back.jpg')
gameicon = pygame.image.load('icon.png')
pygame.display.set_icon(gameicon)

while not game_over:
    if score < 5:
        clock.tick(10)
    if score < 10:
        clock.tick(20)
    if score < 15:
        clock.tick(30)
    if score < 20:
        clock.tick(35)
    if score > 20:
        clock.tick(40)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
     apple_pos = on_grid_random()
     snake.append((0,0))
     score = score + 1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break
    
    if snake[0] in snake[1:]:
        game_over = True
        break

    if game_over:
        break
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    
    if my_direction == UP:
        snake[0] = (snake[0][0], snake [0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake [0][1] + 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake [0][1])
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake [0][1]) 

    screen.fill((0,0,0))
    screen.blit(bg, (0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('comic-sans-ms-4.ttf', 75)
    game_over_screen = game_over_font.render("Pontuação final:" + str(score), True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        if event.type == KEYDOWN: 
            if event.key == K_KP_ENTER:
                pygame.quit()       
            if event.key == K_RETURN:
                pygame.quit()                
            if event.key == K_ESCAPE:
                pygame.quit() 