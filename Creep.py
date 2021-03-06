import random
import pygame
from pygame import Vector2

class Creep:

    def __init__(self):
        self.rayon = 2
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))

    def mourir (self):
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))

    def draw(self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
