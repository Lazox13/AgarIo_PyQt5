import pygame
from pygame.math import Vector2
import core

from Creep import Creep
from Ennemi import Ennemi
from Joueur import Joueur
from TableauDesScores import TableauDesScores


# def afficher_contenu_memory(dico):
#     return [print(f'clef: {k}, valeur: {v}') for k, v in dico.items()]

class AgarIo:
    def __init__(self):

        self.ecran_jeu = core.screen
        self.fps = core.fps = 60
        self.dim_fenetre = core.WINDOW_SIZE = [1080, 720]

        # INITIALISATIONS VARIABLES INDÉPENDANTES DU JOUEUR

        # Choix des paramètres du joueur via menu principal
        # core.memory("nbennemis", MenuParam().nbennemis)

        # Tableau des scores
        self.tableau_scores = core.memory("TableauDesScores", TableauDesScores())
        self.texte_scores = core.memory("TextTabScores", "texte vide")

        # Joueur
        core.memory("Joueur", Joueur())

        # Creeps
        self.tableau_creeps = core.memory("TableauDeCreeps", [])
        for i in range(150):
            self.tableau_creeps.append(Creep())

        # Ennemis
        self.tableau_ennemis = core.memory("TableauEnnemis", [])
        for i in range(5):
            self.tableau_ennemis.append(Ennemi())

        # Taille de la grille
        self.taille_grille = core.memory("TailleGrille", 90)

        # CHOIX DE LA VALEUR DES VARIABLES PAR LE JOUEUR

        # Choix du pseudo par le joueur
        self.nom_joueur = core.memory("PseudoChoisi", input("Veuillez entrer votre pseudo: "))

        # Choix de la couleur du fond par le joueur
        self.choix_couleur_fond = core.memory("choixCouleurFond", input(
            "\n"
            "Veuillez choisir la couleur du fond:\n"
            "Écrire 'clair' pour jouer avec le fond clair.\n"
            "Écrire 'sombre' pour jouer avec le fond sombre.\n"
            "Quel mode choisissez-vous? "))

        if self.choix_couleur_fond == "sombre":
            self.couleur_fond = core.memory("couleurdufond", (40, 40, 40))
            self.couleur_fond_scores = core.memory("couleurdufondscore", (25, 25, 25))
            self.couleur_police_scores = core.memory("couleurpolicescore", (255, 255, 255))
            self.couleur_grille = core.memory("couleurgrille", (100, 100, 100))

        if self.choix_couleur_fond == "clair":
            self.couleur_fond = core.memory("couleurdufond", (255, 255, 255))
            self.couleur_fond_scores = core.memory("couleurdufondscore", (230, 230, 230))
            self.couleur_police_scores = core.memory("couleurpolicescore", (0, 0, 0))
            self.couleur_grille = core.memory("couleurgrille", (150, 150, 150))

        if self.choix_couleur_fond == "exit":
            exit(
                "Test démarrage réussi → jeu fermé intentionnellement !")

        if self.choix_couleur_fond != "clair" and self.choix_couleur_fond != "sombre":
            print("\n"
                  "\n"
                  "[ERREUR] Veuillez entrer un choix valide.\n")

            while self.choix_couleur_fond != "clair" and self.choix_couleur_fond != "sombre":
                self.choix_couleur_fond = core.memory("choixCouleurFond", input(
                    "\n"
                    "Veuillez choisir la couleur du fond:\n"
                    "Écrire 'clair' pour jouer avec le fond clair.\n"
                    "Écrire 'sombre' pour jouer avec le fond sombre.\n"
                    "Quel mode choisissez-vous? \n"))

                if self.choix_couleur_fond == "sombre":
                    self.couleur_fond = core.memory("couleurdufond", (40, 40, 40))
                    self.couleur_fond_scores = core.memory("couleurdufondscore", (25, 25, 25))
                    self.couleur_police_scores = core.memory("couleurpolicescore", (255, 255, 255))
                    self.couleur_grille = core.memory("couleurgrille", (100, 100, 100))

                if self.choix_couleur_fond == "clair":
                    self.couleur_fond = core.memory("couleurdufond", (255, 255, 255))
                    self.couleur_fond_scores = core.memory("couleurdufondscore", (230, 230, 230))
                    self.couleur_police_scores = core.memory("couleurpolicescore", (0, 0, 0))
                    self.couleur_grille = core.memory("couleurgrille", (150, 150, 150))

        print("\n"
              "========== Chargement terminé ! =========="
              "\n")
        # Affichage de tout le dictionnaire
        # afficher_contenu_memory(core.memory("affichage_dico", "Dico affiché"))

        print(f'\n'
              f'Démarrage de la partie de {core.memory("PseudoChoisi")}'
              f'\n')

    def run(self):
        core.cleanScreen()

        # FOND DE LA FENÊTRE DU JEU
        ####################################################################################################################
        # Dessin du fond
        pygame.draw.rect(core.screen, self.choix_couleur_fond, pygame.Rect(0, 0, 1080, 720))

        # Dessin de la grille
        for x in range(0, 1080, self.taille_grille):
            for y in range(0, 720, self.taille_grille):
                rect = pygame.Rect(x, y, self.taille_grille, self.taille_grille)
                pygame.draw.rect(self.ecran_jeu, self.taille_grille, rect, 1)

        # Bloc collisions
        # ======================================================================================================
        for creep in self.tableau_creeps:
            # [Collision] Joueur mange Creeps
            if creep.position.distance_to(Joueur().position) < Joueur().rayon + creep.rayon:
                creep.mourir()
                Joueur().grossir()
                self.tableau_scores.compteurCreeps = self.tableau_scores.compteurCreeps + 1

            # [Collision] Ennemis mangent Creeps
            for ennemi in self.tableau_ennemis:
                ennemi.perception(ennemi, creep, Joueur())
                # if e.ChampVisionEnnemi_resultat == 1:
                # e.deplacement_versCreep(720, 1080, c)
                if creep.position.distance_to(ennemi.position) < ennemi.rayon + creep.rayon:
                    creep.mourir()
                    ennemi.grossir()

        # [Collision] Ennemis/Joueur
        for ennemi in self.tableau_ennemis:
            if ennemi.position.distance_to(Joueur().position) < Joueur().rayon + ennemi.rayon:
                # Joueur mange ennemis
                if Joueur().rayon >= ennemi.rayon:
                    ennemi.mourir()
                    Joueur().grossir()
                    self.tableau_scores.compteurEnnemis = self.tableau_scores.compteurEnnemis + 1
                # Ennemis mangent joueur
                else:
                    Joueur().mourir()

        # Bloc dessins
        # =========================================================================================================
        # Dessins des creeps
        for c in self.tableau_creeps:
            c.draw(core.screen)

        # Dessins des ennemis
        for dessin_e in self.tableau_ennemis:
            dessin_e.draw(core.screen)

        # Dessin du joueur
        Joueur().draw(self.ecran_jeu)

        # Bloc déplacements
        # ====================================================================================================
        # Déplacements du joueur
        Joueur().deplacer(core.getMouseLeftClick(), 720, 1080)

        # Déplacements des ennemis (si aucune détection) → déplacements aléatoires
        for deplacementsEnnemis in self.tableau_ennemis:
            deplacementsEnnemis.deplacement_aleatoire(720, 1080)
            # e.deplacement_versCreep(720,1080,c)

        # Bloc scores
        # ====================================================================================================
        # Dessin du rectangle pour les scores
        self.tableau_scores.dessiner(self.ecran_jeu, self.couleur_fond_scores)

        # Affichage du pseudo choisi par le joueur
        self.texte_scores = self.tableau_scores.police.render("Joueur: " + str(self.nom_joueur), False,
                                                              self.couleur_police_scores)
        self.ecran_jeu.blit(self.texte_scores, (8, 6))

        # Affichage du rayon du joueur
        self.texte_scores = self.tableau_scores.police.render("Joueur: " + str(Joueur().rayon), False,
                                                              self.couleur_police_scores)
        self.ecran_jeu.blit(self.texte_scores, (8, 30))

        # Affichage des creeps mangés par le joueur
        self.texte_scores = self.tableau_scores.police.render("Joueur: " + str(self.tableau_scores.compteurCreeps), False,
                                                              self.couleur_police_scores)
        self.ecran_jeu.blit(self.texte_scores, (8, 54))

        # Affichage des ennemis mangés par le joueur
        self.texte_scores = self.tableau_scores.police.render("Joueur: " + str(self.tableau_scores.compteurEnnemis),
                                                              False,
                                                              self.couleur_police_scores)
        self.ecran_jeu.blit(self.texte_scores, (8, 78))

        if Joueur().rayon_max == 150:
            print("Fin de la partie de", self.nom_joueur, "\n")
            exit("BARVO: Vous avez atteint le rayon maximum!")


    core.main(core.setup, run)
