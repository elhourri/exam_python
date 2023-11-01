def calculer_cout_total(duree):
    offres = [
        {"nom": "Illimité (200DH)", "minutes_gratuites": float('inf'), "cout_par_minute": 0},
        {"nom": "2 heures (100DH)", "minutes_gratuites": 120, "cout_par_minute": 0.5},
        {"nom": "1 heure (50DH)", "minutes_gratuites": 60, "cout_par_minute": 1},
        {"nom": "30 minutes (20DH)", "minutes_gratuites": 30, "cout_par_minute": 1.5},
        {"nom": "0DH (2DH par minute)", "minutes_gratuites": 0, "cout_par_minute": 2}
    ]

    couts = []

    for offre in offres:
        if duree <= offre["minutes_gratuites"]:
            cout_total = 0
        else:
            cout_total = (duree - offre["minutes_gratuites"]) * offre["cout_par_minute"]
        couts.append(cout_total)

    return couts

def afficher_menu():
    print("Menu :")
    print("1 - Entrer la durée de communication")
    print("2 - Afficher le coût mensuel par offre")
    print("3 - Afficher l'offre la plus intéressante (moins cher)")
    print("4 - Quitter le programme")

duree = 0

while True:
    afficher_menu()
    choix = int(input("Faites votre choix : "))

    if choix == 1:
        duree_communication = int(input("Entrez la durée de communication du mois en minutes : "))
    elif choix == 2:
        if duree_communication != 0:
            couts_mensuels = calculer_cout_total(duree_communication)
            print("Coût mensuel par offre :", couts_mensuels)
        else:
            print("Veuillez d'abord entrer la durée de communication.")
    elif choix == 3:
        if duree_communication != 0:
            couts_mensuels = calculer_cout_total(duree_communication)
            cout_min = min(couts_mensuels)
            index = couts_mensuels.index(cout_min)
            print(f"L'offre la plus intéressante est l'offre {index + 1} avec un coût de {cout_min} DH")
        else:
            print("Veuillez d'abord entrer la durée de communication.")
