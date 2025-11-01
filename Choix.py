import random
import time
continuer = "o"

input("Binvenue sur ton tirage de nombre aléatoire.\nAppuie sur entre pour commencer [<⨼]")

while continuer == "o":
    while True:
        try:
            a = int(input("Entre ton premier nombre entier.\n"))
            break
        except ValueError:
            print("Erreur: entrer une valeur valide.")
    while True:
        try:
            b = int(input("Entre ton deuxième nombre entier. (Attention: Il doit être supérieur au premier.)\n"))
            if b <= a:
                print("Erreur: Ton deuxième nombre doit être supérieur au premier")
            else:
                break
        except ValueError:
            print("Erreur: entrer une valeur valide.")

    c = random.randint(a, b)
    print("------\nLe nombre tiré entre", a, "et", b, "est", c, "\n------")
    time.sleep(0.5)
    while True:
        try:
            continuer = str(input("Veux-tu tirer un nouveau nombre ? oui=o non=n\n")).strip().lower()
            if continuer == "o" or continuer == "n":
                break
            print("Erreur: réponsse non comprise.")
        except ValueError:
            print("Erreur: réponsse non comprise.")
print("Au revoir.")