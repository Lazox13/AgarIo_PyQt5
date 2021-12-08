import random
import pygame
from pygame import Vector2

class Ennemi:

    def __init__(self):
        self.rayon = 5
        self.couleur = (random.randint(40, 240), 0, 0)
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))
        self.nom = "ENNEMI"

        self.direction = Vector2(0, 0)
        self.raideur = 0.00025
        self.vitesse = 1
        self.vitessemax = 2
        self.Fx = 0
        self.Ux = Vector2(0, 0)
        self.l = 0
        self.l0 = 10
        self.L = 0

        self.ChampVisionEnnemi = 60
        self.ChampVisionEnnemi_resultat = 0

    def mourir (self):
        self.rayon = 5
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))


    def draw(self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

    def perception(self,ennemiEnMvmt, creep, joueur):
        #for self.rayon in Vector2(5,150):

        if ennemiEnMvmt.position.distance_to(creep.position) < self.ChampVisionEnnemi - creep.rayon :
            self.ChampVisionEnnemi_resultat = 1 # creep_trouvé

        if ennemiEnMvmt.position.distance_to(joueur.position) < self.ChampVisionEnnemi - joueur.rayon:
            self.ChampVisionEnnemi_resultat = 3  # joueur_trouvé

        #if ennemiEnMvmt.position.distance_to(autreEnnemi.position) < self.ChampVisionEnnemi - autreEnnemi.rayon and ennemiEnMvmt.rayon < autreEnnemi.rayon:
            #self.ChampVisionEnnemi_resultat = 2 # autreEnnemi_trouvé

    def grossir(self):
        if self.rayon < 150:
            self.rayon = self.rayon + 1
            self.ChampVisionEnnemi = self.rayon + 6

            self.vitessemax = self.vitessemax * 0.988
            self.Fx = self.vitesse * self.Fx

    def deplacement_aleatoire(self,h,l):
        self.Fx = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        self.direction = self.direction + self.Fx

        if self.direction.length() > self.vitessemax and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(0, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)

    def fuite(self,h,l,j,detection):

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(0, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)


        if detection is not None:

            self.Ux = j - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)

            self.Fx = self.raideur * self.L * self.Ux
            self.direction = self.direction + self.Fx

        else:
            self.Ux = Vector2(0, 0)


        if self.direction.length() > self.vitessemax and self.direction.length() !=0 :
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position

    def deplacement_versCreep(self,h,l,creep):
        #self.Fx = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        self.Ux = creep.position - self.position
        self.l = self.Ux.length()
        self.Ux = self.Ux.normalize()
        self.L = abs(self.l - self.l0)

        self.Fx = self.raideur * self.L * self.Ux
        self.direction = self.direction + self.Fx

        self.Ux = Vector2(0, 0)

        if self.direction.length() > self.vitessemax and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(0, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)