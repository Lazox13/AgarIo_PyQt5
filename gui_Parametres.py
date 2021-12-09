import pygame
from pygame.math import Vector2
import core

from Creep import Creep
from Ennemi import Ennemi
from Joueur import Joueur
from TableauDesScores import TableauDesScores


class AgarIo:
    def __init__(self):
        self.contenu_dico = core.memory("contenu_dico", 1)
        self.ecran_jeu = core.screen
        self.fps = core.fps = 60
        self.dim_fenetre = core.WINDOW_SIZE = [1080, 720]

    def afficher_contenu_memory(self):
        return [print(f'clef: {k}, valeur: {v}') for k, v in self.contenu_dico.items()]

    def run(self):
        self.ecran_jeu.show()

    core.main(core.setup, run)
