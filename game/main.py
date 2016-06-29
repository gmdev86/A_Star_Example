import pygame, sys, Funk
from tileC import Tile
from object_classes import *
from interaction import interaction
from A_Star import A_Star

pygame.init()
pygame.font.init()

invalids = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 37, 55, 73, 91, 109, 127, 145, 163, 181,
            182, 183, 184, 185, 186, 187, 188, 189, 190,
            191, 192, 193, 194, 195, 196, 197, 198,
            36, 54, 72, 90, 108, 126, 144, 162, 180, 198)

screen = pygame.display.set_mode((720, 440))

for y in range(0, screen.get_height(), 40):
    for x in range(0, screen.get_width(), 40):
        if Tile.total_tiles in invalids:
            Tile(x, y, 'solid')
        else:
            Tile(x, y, 'empty')

clock = pygame.time.Clock()
FPS = 24
total_frames = 0

zombie1 = Zombie(200, 240)
survivor = Survivor(400, 120)

while True:
    screen.fill([0, 0, 0])
    A_Star(screen, survivor)
    interaction(screen, survivor)
    Tile.draw_tiles(screen)
    survivor.draw(screen)
    Zombie.draw_zombies(screen)

    pygame.display.flip()
    clock.tick(FPS)
    total_frames += 1
