import pygame
import random
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Желтый круг')
    size = width, height = random.randint(1, 1920), random.randint(1, 1080)
    screen = pygame.display.set_mode(size)
    running = True
    v = 0  # пикселей в секунду
    clock = pygame.time.Clock()
    raduisius = 0
    coord_x = 0
    coord_y = 0
    prosto_per = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 255))
        if event.type == pygame.MOUSEBUTTONDOWN:
            v = 10
            raduisius += v * clock.tick() / 1000
            coord_x, coord_y = event.pos
            raduisius = 0
            prosto_per += 1
        if event.type == pygame.MOUSEBUTTONUP:
            v = 10
            raduisius += v * clock.tick() / 1000
        if event.type == pygame.MOUSEMOTION:
            v = 10
            raduisius += v * clock.tick() / 1000
        if prosto_per >= 1:
            pygame.draw.circle(screen, (255, 255, 0), (coord_x, coord_y), raduisius)
        pygame.display.flip()
    pygame.quit()