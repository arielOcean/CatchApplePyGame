import pygame
import random
from pygame.color import THECOLORS

pygame.init()
pygame.display.set_caption("Catch The Apple")
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# параметры яблока
circle_radius = 10
circle_speed = 3
circle_color = THECOLORS['red2']
circle_pos = [screen_width//2, circle_radius]
circle_landed = False

#параметры корзины
bag_height = 20
bag_width = 100
bag_x = screen_width//2 - bag_width//2

#количество яблок
apple_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bag_x -= 20
            elif event.key == pygame.K_RIGHT:
                bag_x += 20

    # яблоко падает вниз
    circle_pos[1] += circle_speed

    # проверяем, упало ли яблоко
    if circle_pos[1] + circle_radius > screen_height:
        if bag_x < circle_pos[0] < bag_x+bag_width:
            apple_count += 1
        circle_pos[0] = random.randint(circle_radius, screen_width//2 - circle_radius)
        circle_pos[1] = circle_radius


    # рисование
    screen.fill(THECOLORS['seagreen2'])

    font = pygame.font.SysFont('couriernew', 18)
    text = font.render(str('Яблок в корзине: ' + str(apple_count)), True, THECOLORS['darkorange'])
    screen.blit(text, (8, 8))

    rect = pygame.Rect(bag_x, screen_height - bag_height, bag_width, bag_height)
    pygame.draw.rect(screen,  THECOLORS['aquamarine'], rect, 0)

    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)

    pygame.display.update()

    # частота обновления экрана
    pygame.time.Clock().tick(60)
