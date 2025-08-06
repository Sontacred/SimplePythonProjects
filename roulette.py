import random

def charger_barillet():
    barillet = ["balle"] + ["vide"] * 5
    random.shuffle(barillet)
    return barillet

def tirer(barillet, cible):
    tir = barillet.pop(0)
    if tir == "balle":
        print(f"💥 Bang ! {cible} est mort.\nPartie terminée.")
        return False
    else:
        print(f"Clic... {cible} est sauf.")
        return True

# Initialisation
barillet = charger_barillet()
game_status = True

# Boucle principale
while game_status and barillet:
    # TOUR DU JOUEUR
    print("\nTon tour :")
    print("[1] - Tirer sur toi-même\n[2] - Tirer sur l'adversaire")
    case = input("Choisir une option : ")

    if case == "1":
        game_status = tirer(barillet, "Le joueur")

        if game_status and barillet:
            # Seconde chance pour le joueur
            print("\nTu as une deuxième chance ! Que veux-tu faire ?")
            print("[1] - Re-tirer sur toi-même\n[2] - Tirer sur l'adversaire")
            seconde_choix = input("Choisir une option : ")
            if seconde_choix == "1":
                game_status = tirer(barillet, "Le joueur")
            elif seconde_choix == "2":
                game_status = tirer(barillet, "L'adversaire")
            else:
                print("Choix invalide, on passe au tour de l'adversaire.")

    elif case == "2":
        game_status = tirer(barillet, "L'adversaire")
    else:
        print("Choix invalide")
        continue  # Recommence ce tour

    if not game_status or not barillet:
        break

    # TOUR DE L'ADVERSAIRE (IA)
    print("\nTour de l'adversaire :")
    choix_ia = random.choice(["1", "2"])
    if choix_ia == "1":
        print("L'adversaire tire sur lui-même...")
        game_status = tirer(barillet, "L'adversaire")

        if game_status and barillet:
            # Deuxième choix de l'adversaire
            second_choix_ia = random.choice(["1", "2"])
            if second_choix_ia == "1":
                print("L'adversaire retente sa chance sur lui-même...")
                game_status = tirer(barillet, "L'adversaire")
            else:
                print("L'adversaire décide de te viser cette fois...")
                game_status = tirer(barillet, "Le joueur")

    else:
        print("L'adversaire te vise...")
        game_status = tirer(barillet, "Le joueur")
