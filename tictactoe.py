###########################################
# Auteurs :
# Nom, Prénom, DA <username github>
# Nom, Prénom, DA <username github>
# Nom, Prénom, DA <username github>
###########################################

def afficher_grille(grille):
    print("\n")
    for i in range(3):
        ligne = " | ".join(str(grille[j]) for j in range(i * 3, (i + 1) * 3))
        print(f" {ligne} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def cellule_valide(grille, cellule):
    # TODO 2: Vérifier si la cellule saisie est valide

    return True

def verifier_victoire(grille, joueur):
    # TODO 3: Vérifier si un joueur remporte la partie

    return False

def faire_une_partie():
    # TODO 1a: Remplacer la grille ci-dessous en utilisant une liste en compréhension
    grille = [1,2,3,4,5,6,7,8,9]

    joueur = "X"
    tour = 0

    while tour < 9:
        afficher_grille(grille)

        # TODO 1b: demander au joueur d'entrer son choix de cellule
        cellule = 0

        if not cellule_valide(grille, cellule):
            print("❌ Case invalide, réessayez.")
            continue

        grille[cellule] = joueur
        tour += 1

        if verifier_victoire(grille,joueur):
            afficher_grille(grille)
            print(f"🎉 Le joueur {joueur} a gagné !")
            # TODO 1c: retourne un dictionnaire
            return None

        joueur = "O" if joueur == "X" else "X"

    afficher_grille(grille)
    print("🤝 Match nul !")
    # TODO 1c: retourne un dictionnaire
    return None

def jouer():
    # TODO 4: comptabiliser des statistiques et jouer plusieurs fois
    faire_une_partie()

jouer()
