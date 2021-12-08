import pygame
import core


from Creep import Creep
from Ennemi import Ennemi
from Joueur import Joueur
from TableauDesScores import TableauDesScores

print("test")

from gui_main import MenuParam



# def afficher_contenu_memory(dico):
#     return [print(f'clef: {k}, valeur: {v}') for k, v in dico.items()]


def setup():
    print("\nDémarrage d'agar.io - MORMONT • ROLLET")
    print("-------- Initialisation variables... --------\n")
    core.fps = 60
    core.WINDOW_SIZE = [1080, 720]

    # TEST AVEC PC MATEO
    Menu = MenuParam()
    print(int(Menu.nbennemis))

    # INITIALISATIONS VARIABLES INDÉPENDANTES DU JOUEUR

    # Choix des paramètres du joueur via menu principal
    # core.memory("nbennemis", MenuParam().nbennemis)

    # Tableau des scores
    core.memory("TableauDesScores", TableauDesScores())
    core.memory("TextTabScores", "texte vide")

    # Joueur
    core.memory("Joueur", Joueur())

    # Creeps
    core.memory("TableauDeCreeps", [])
    for i in range(150):
        core.memory("TableauDeCreeps").append(Creep())

    # Ennemis
    #core.memory("nb_ennemis", input("nombre d'ennemis : "))
    core.memory("TableauEnnemis", [])
    for i in range(int(Menu.nbennemis)):
        core.memory("TableauEnnemis").append(Ennemi())

    # Taille de la grille
    core.memory("TailleGrille", 90)

    # CHOIX DE LA VALEUR DES VARIABLES PAR LE JOUEUR

    # Choix du pseudo par le joueur
    core.memory("PseudoChoisi", input("Veuillez entrer votre pseudo: "))

    # Choix de la couleur du fond par le joueur
    core.memory("choixCouleurFond", input(
        "\n"
        "Veuillez choisir la couleur du fond:\n"
        "Écrire 'clair' pour jouer avec le fond clair.\n"
        "Écrire 'sombre' pour jouer avec le fond sombre.\n"
        "Quel mode choisissez-vous? "))

    if core.memory("choixCouleurFond") == "sombre":
        core.memory("couleurdufond", (40, 40, 40))
        core.memory("couleurdufondscore", (25, 25, 25))
        core.memory("couleurpolicescore", (255, 255, 255))
        core.memory("couleurgrille", (100, 100, 100))

    if core.memory("choixCouleurFond") == "clair":
        core.memory("couleurdufond", (255, 255, 255))
        core.memory("couleurdufondscore", (230, 230, 230))
        core.memory("couleurpolicescore", (0, 0, 0))
        core.memory("couleurgrille", (150, 150, 150))

    if core.memory("choixCouleurFond") == "exit":
        exit(
            "Test démarrage réussi → jeu fermé intentionnellement !")

    if core.memory("choixCouleurFond") != "clair" and core.memory("choixCouleurFond") != "sombre":
        print("\n"
              "\n"
              "[ERREUR] Veuillez entrer un choix valide.\n")

        while core.memory("choixCouleurFond") != "clair" and core.memory("choixCouleurFond") != "sombre":
            core.memory("choixCouleurFond", input(
                "\n"
                "Veuillez choisir la couleur du fond:\n"
                "Écrire 'clair' pour jouer avec le fond clair.\n"
                "Écrire 'sombre' pour jouer avec le fond sombre.\n"
                "Quel mode choisissez-vous? "))

            print("\n")
            if core.memory("choixCouleurFond") == "sombre":
                core.memory("couleurdufond", (40, 40, 40))
                core.memory("couleurdufondscore", (25, 25, 25))
                core.memory("couleurpolicescore", (255, 255, 255))
                core.memory("couleurgrille", (100, 100, 100))

            if core.memory("choixCouleurFond") == "clair":
                core.memory("couleurdufond", (255, 255, 255))
                core.memory("couleurdufondscore", (230, 230, 230))
                core.memory("couleurpolicescore", (0, 0, 0))
                core.memory("couleurgrille", (150, 150, 150))



    print("\n"
          "========== Chargement terminé ! =========="
          "\n")
    # Affichage de tout le dictionnaire
    #afficher_contenu_memory(core.memory("affichage_dico", "Dico affiché"))

    print(f'\n'
          f'Démarrage de la partie de {core.memory("PseudoChoisi")}'
          f'\n')

def run():
    core.cleanScreen()

    # FOND DE LA FENÊTRE DU JEU
    ####################################################################################################################
    # Dessin du fond
    pygame.draw.rect(core.screen, core.memory("couleurdufond"), pygame.Rect(0, 0, 1080, 720))

    # Dessin de la grille
    for x in range(0, 1080, core.memory("TailleGrille")):
        for y in range(0, 720, core.memory("TailleGrille")):
            rect = pygame.Rect(x, y, core.memory("TailleGrille"), core.memory("TailleGrille"))
            pygame.draw.rect(core.screen, core.memory("couleurgrille"), rect, 1)

    # Bloc collisions
    # ======================================================================================================
    for c in core.memory("TableauDeCreeps"):
        # [Collision] Joueur mange Creeps
        if c.position.distance_to(core.memory("Joueur").position) < core.memory("Joueur").rayon + c.rayon:
            c.mourir()
            core.memory("Joueur").grossir()
            core.memory("TableauDesScores").compteurCreeps = core.memory("TableauDesScores").compteurCreeps + 1

        # [Collision] Ennemis mangent Creeps
        for ennemi in core.memory("TableauEnnemis"):
            ennemi.perception(ennemi, c, core.memory("Joueur"))
            # if e.ChampVisionEnnemi_resultat == 1:
            # e.deplacement_versCreep(720, 1080, c)
            if c.position.distance_to(ennemi.position) < ennemi.rayon + c.rayon:
                c.mourir()
                ennemi.grossir()

    # [Collision] Ennemis/Joueur
    for ennemi in core.memory("TableauEnnemis"):
        if ennemi.position.distance_to(core.memory("Joueur").position) < core.memory("Joueur").rayon + ennemi.rayon:
            # Joueur mange ennemis
            if core.memory("Joueur").rayon >= ennemi.rayon:
                ennemi.mourir()
                core.memory("Joueur").grossir()
                core.memory("TableauDesScores").compteurEnnemis = core.memory("TableauDesScores").compteurEnnemis + 1
            # Ennemis mangent joueur
            else:
                core.memory("Joueur").mourir()

    # Bloc dessins
    # =========================================================================================================
    # Dessins des creeps
    for c in core.memory("TableauDeCreeps"):
        c.draw(core.screen)

    # Dessins des ennemis
    for dessin_e in core.memory("TableauEnnemis"):
        dessin_e.draw(core.screen)

    # Dessin du joueur
    core.memory("Joueur").draw(core.screen)

    # Bloc déplacements
    # ====================================================================================================
    # Déplacements du joueur
    core.memory("Joueur").deplacer(core.getMouseLeftClick(), 720, 1080)

    # Déplacements des ennemis (si aucune détection) → déplacements aléatoires
    for deplacementsEnnemis in core.memory("TableauEnnemis"):
        deplacementsEnnemis.deplacement_aleatoire(720, 1080)
        # e.deplacement_versCreep(720,1080,c)

    # Bloc scores
    # ====================================================================================================
    # Dessin du rectangle pour les scores
    core.memory("TableauDesScores").dessiner(core.screen, core.memory("couleurdufondscore"))

    # Affichage du pseudo choisi par le joueur
    core.memory("TextTabScores",
                core.memory("TableauDesScores").police.render("Joueur: " + str(core.memory("PseudoChoisi")), False,
                                                              core.memory("couleurpolicescore")))
    core.screen.blit(core.memory("TextTabScores"), (8, 6))

    # Affichage du rayon du joueur
    core.memory("TextTabScores",
                core.memory("TableauDesScores").police.render("Rayon du joueur: " + str(core.memory("Joueur").rayon),
                                                              False, core.memory("couleurpolicescore")))
    core.screen.blit(core.memory("TextTabScores"), (8, 30))

    # Affichage des creeps mangés par le joueur
    core.memory("TextTabScores", core.memory("TableauDesScores").police.render(
        "Creeps mangés: " + str(core.memory("TableauDesScores").compteurCreeps), False,
        core.memory("couleurpolicescore")))
    core.screen.blit(core.memory("TextTabScores"), (8, 54))

    # Affichage des ennemis mangés par le joueur
    core.memory("TextTabScores", core.memory("TableauDesScores").police.render(
        "Ennemis mangés: " + str(core.memory("TableauDesScores").compteurEnnemis), False,
        core.memory("couleurpolicescore")))
    core.screen.blit(core.memory("TextTabScores"), (8, 78))

    if core.memory("Joueur").rayon == 150:
        print("Fin de la partie de", core.memory("PseudoChoisi"), "\n")
        exit("BARVO: Vous avez atteint le rayon maximum!")


core.main(setup, run)
