import os
import sys

import pygame

# Изображение не получится загрузить

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Изображения")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

surfing = load_image('one.jpg', -1)
image1 = pygame.transform.scale(surfing, (200, 100))
image2 = pygame.transform.scale(surfing, (100, 200))
car_rect = surfing.get_rect(center=(1200 // 2, 1200 // 2))
car_rect1 = image1.get_rect(center=(200 // 2, 200 // 2))
car_rect2 = image1.get_rect(center=(700 // 2, 700 // 2))
screen.blit(surfing, car_rect)
screen.blit(image1, car_rect1)
screen.blit(image2, car_rect2)
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()