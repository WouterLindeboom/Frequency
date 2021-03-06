import pygame

from Board.Buildings.Building import Building


class Barracks(Building):
    def __init__(self, player, tile):
        self.Textures = [
            pygame.transform.scale(pygame.image.load('images/buildings/barracksGreen.png').convert_alpha(), [35, 35]),
            pygame.transform.scale(pygame.image.load('images/buildings/barracksBlue.png').convert_alpha(), [35, 35]),
            pygame.transform.scale(pygame.image.load('images/buildings/barracksYellow.png').convert_alpha(), [35, 35]),
            pygame.transform.scale(pygame.image.load('images/buildings/barracksRed.png').convert_alpha(), [35, 35])
        ]
        super().__init__(player, tile, self.Textures)
