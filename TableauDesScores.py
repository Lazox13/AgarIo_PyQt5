import pygame
from pygame.math import Vector2

from Creep import Creep
from Ennemi import Ennemi
from Joueur import Joueur

class TableauDesScores:

    def __init__(self):
        pygame.font.init()
        self.police = (pygame.font.SysFont('Calibri', 22))
        self.compteurEnnemis = 0
        self.compteurCreeps = 0

    def dessiner(self,screen,couleurFond):
        pygame.draw.rect(screen, couleurFond, pygame.Rect(5, 5, 200, 100))
