import pygame
from pygame.surface import Surface


from Helpers.EventHelpers import EventExist
from Vector2 import Vector2


class BuyUnitItem:
    def __init__(self, offset: Vector2, playingPlayer, image: Surface=None, hover: Surface=None, rect=None):
        self.Offset = offset
        self.Image = image if image is not None else self._getTexture()
        self.Hover = hover if hover is not None else self._getHoverTexture()
        self.Rect = rect
        self.PlayingPlayer = playingPlayer

    def Update(self, game):
        return self

    def Draw(self, game):
        # Extra screen-based properties

        margin = 38 + 20

        x = 10 + margin * self.Offset.X
        y = self.Offset.Y

        self.Rect = game.Settings.GetScreen().blit(self.Image, (x, y))

    def IsHoverdByMouse(self):
        return self.Rect is not None and self.Rect.collidepoint(pygame.mouse.get_pos())

    def IsClickedByMouse(self, game):
        return self.IsHoverdByMouse() and EventExist(game.Events, pygame.MOUSEBUTTONUP)

    def _getTexture(self):
        return None

    def _getHoverTexture(self):
        return None


class SoldierButton(BuyUnitItem):

    def _getTexture(self):
        return pygame.transform.scale(pygame.image.load('images/units/soldierGreen.png').convert_alpha(), (38, 38))

    def _getHoverTexture(self):
        return pygame.transform.scale(pygame.image.load('images/units/soldierRed.png').convert_alpha(), (38, 38))

class RobotButton(BuyUnitItem):

    def _getTexture(self):
        return pygame.transform.scale(pygame.image.load('images/units/robotGreen.png').convert_alpha(), (38, 38))

    def _getHoverTexture(self):
        return pygame.transform.scale(pygame.image.load('images/units/robotRed.png').convert_alpha(), (38, 38))

class TankButton(BuyUnitItem):

    def _getTexture(self):
        return pygame.transform.scale(pygame.image.load('images/units/tankGreen.png').convert_alpha(), (38, 38))

    def _getHoverTexture(self):
        return pygame.transform.scale(pygame.image.load('images/units/tankRed.png').convert_alpha(), (38, 38))

class BoatButton(BuyUnitItem):

    def _getTexture(self):
        return pygame.transform.scale(pygame.image.load('images/units/shipGreen.png').convert_alpha(), (38, 38))

    def _getHoverTexture(self):
        return pygame.transform.scale(pygame.image.load('images/units/shipRed.png').convert_alpha(), (38, 38))
