#près requis
import random
import time

def Accueil():
    choixjeu = [1, 2, 3, 4]
    print("Choisis t'a difficulter\nFacile : 'Tape 1' ; Intermediaire : 'Tape 2' ; Difficile : 'Tape 3'\nTape '4' pour quitter le jeu.")
    while True:
        try:
            Diff = int(input("Tape le nombre de ta difficulter\n"))
            if Diff in choixjeu:
                break
            print("Erreur : Entrer une valeur correct")
        except ValueError:
            print("Erreur : Entrer une valeur correct")
    return(Diff)

#Accueil
input("Bienvenue sur le jeu 'Devine le Nombre'\nAppuie sur 'Entrer' pour commencer")
while True:
    Nbcoup = 0
    Diff = Accueil()

    #difficulter 1
    if Diff == 1:
            #choix du bot
            NbUn = list(range(1, 11))
            choixBot = random.choice(NbUn)
            print("Le bot a choisis son nombre")
            time.sleep(1)
            #choix utilisateur
            while True:
                while True:
                    try:
                        choixUser = int(input("Trouve ce nombre. Il est entre 1 et 10 (inclut)\n"))
                        if choixUser in NbUn:
                            break
                        else:
                            print("Erreur : choisis un nombre entre 1 et 10")
                            time.sleep(0.5)
                    except ValueError:
                        print("Erreur : choisis un nombre entre 1 et 10")
                        time.sleep(0.5)

                #supérieur, inférieur ou égal
                Nbcoup = Nbcoup + 1
                if choixUser < choixBot:
                    print("Mon nombre est superieur à", choixUser)
                elif choixUser > choixBot:
                    print("Mon nombre est inferieur à", choixUser)
                else:
                    print("Bravo ! Tu as trouvé en", Nbcoup, "coup")
                    time.sleep(1)
                    input("Appuie sur entrer pour retourner à l'accueil\n")
                    break

    #difficulter 2
    if Diff == 2:
            #choix du bot
            NbDeux = list(range(1, 50))
            choixBot = random.choice(NbDeux)
            print("Le bot a choisis son nombre")
            time.sleep(1)
            #choix utilisateur
            while True:
                while True:
                    try:
                        choixUser = int(input("Trouve ce nombre. Il est entre 1 et 50 (inclut)\n"))
                        if choixUser in NbDeux:
                            break
                        else:
                            print("Erreur : choisis un nombre entre 1 et 50")
                            time.sleep(0.5)
                    except ValueError:
                        print("Erreur : choisis un nombre entre 1 et 50")
                        time.sleep(0.5)

                #supérieur, inférieur ou égal
                Nbcoup = Nbcoup + 1
                if choixUser < choixBot:
                    print("Mon nombre est superieur à", choixUser)
                elif choixUser > choixBot:
                    print("Mon nombre est inferieur à", choixUser)
                else:
                    print("Bravo ! Tu as trouvé en", Nbcoup, "coup")
                    time.sleep(1)
                    input("Appuie sur entrer pour retourner à l'accueil\n")
                    break

    #difficulter 3
    if Diff == 3:
            #choix du bot
            NbTrois = list(range(1, 101))
            choixBot = random.choice(NbTrois)
            print("Le bot a choisis son nombre")
            time.sleep(1)
            #choix utilisateur
            while True:
                while True:
                    try:
                        choixUser = int(input("Trouve ce nombre. Il est entre 1 et 100 (inclut)\n"))
                        if choixUser in NbTrois:
                            break
                        else:
                            print("Erreur : choisis un nombre entre 1 et 100")
                            time.sleep(0.5)
                    except ValueError:
                        print("Erreur : choisis un nombre entre 1 et 100")
                        time.sleep(0.5)

                #supérieur, inférieur ou égal
                Nbcoup = Nbcoup + 1
                if choixUser < choixBot:
                    print("Mon nombre est superieur à", choixUser)
                elif choixUser > choixBot:
                    print("Mon nombre est inferieur à", choixUser)
                else:
                    print("Bravo ! Tu as trouvé en", Nbcoup, "coup")
                    time.sleep(1)
                    input("Appuie sur entrer pour retourner à l'accueil\n")
                    break
    
    #sortie programme
    if Diff == 4:
        print("Au revoir et à bientôt.\nJ'espère que tu t'es ammuser.")
        break