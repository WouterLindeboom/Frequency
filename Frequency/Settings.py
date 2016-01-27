﻿import pygame
from pygame.surface import Surface

from Vector2 import Vector2


class GameSettings:


    def __init__(self, resolution: Vector2 = Vector2(1280, 800),
                 screen: Surface = None,
                 tileSize = None,
                 newPlayers = 0,
                 mapSize = None,
                 menuLeftSize = None,
                 selectedUnitBuilding = "Barracks"):

        self.Resolution = resolution
        self.TileSize = tileSize
        self.newPlayer = newPlayers
        self.MapSize = mapSize
        self.MenuLeftSize = menuLeftSize
        self.SelectedUnitBuilding = selectedUnitBuilding

        self.screen = screen if screen is not None \
            else pygame.display.set_mode([resolution.X, resolution.Y])

        self.SetMaxTiles(Vector2(18, 18))
        self.Players = newPlayers

    def updateResolution(self, newResolution):
        self.Resolution = newResolution

    def GetScreen(self):
        return self.screen

    def SetMaxTiles(self, maxTiles):
        self.MaxTiles = maxTiles

    def GetMaxTiles(self):
        return self.MaxTiles

    def SetMapSize(self, mapSize):
        self.MapSize = mapSize

    def GetMapSize(self):
        return self.MapSize

    def SetMenuLeftSize(self, menuSize):
            self.MenuLeftSize = menuSize

    def GetMenuLeftSize(self):
        return self.MenuLeftSize

    def UpdatePlayers(self, newPlayers):
        self.Players = newPlayers

    def GetTotalPlayers(self):
        return self.Players

    def SetSelectedUnitBuilding(self, selectedUnitBuilding):
        self.SelectedUnitBuilding = selectedUnitBuilding

    def GetSelectedUnitBuilding(self):
        return self.SelectedUnitBuilding