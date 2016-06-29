import pygame
import Funk


class Tile(pygame.Rect):

    List = []
    width, height = 40, 40
    total_tiles = 1
    H, V = 1, 18

    def __init__(self, x, y, Type):

        self.parent = None
        self.H, self.G, self.F = 0, 0, 0

        self.type = Type
        self.number = Tile.total_tiles
        Tile.total_tiles += 1

        if Type == 'empty':
            self.walkable = True
        else:
            self.walkable = False

        pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) )

        Tile.List.append(self)

    @staticmethod
    def get_tile(number):
        for tile in Tile.List:
            if tile.number == number:
                return tile

    @staticmethod
    def draw_tiles(screen):
        half = Tile.width / 2

        for tile in Tile.List:

            if not(tile.type == 'empty'):
                pygame.draw.rect(screen, [40, 40, 40], tile)

            if tile.G != 0:
                Funk.text_to_screen(screen, tile.G, tile.x, tile.y + half, 15, color=[120, 157, 40])
            if tile.H != 0:
                Funk.text_to_screen(screen, tile.H, tile.x + half, tile.y + half, 15, color=[20, 67, 150])
            if tile.F != 0:
                Funk.text_to_screen(screen, tile.F, tile.x + half, tile.y, 15, color=[56, 177, 177])

            # Funk.text_to_screen(screen, tile.number, tile.x, tile.y)

    def __str__(self):
        return str(self.number)
