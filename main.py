#Accueil
print("Bienvenue sur le simulateur : 'Pair ou Impair'")
input("Appuyez sur entrer pour continuer")
c="o"
while c=="o":
    #demander une valeur
    while True :
        try:
            u=int(input("Veuillez entrer un nombre entier : "))
            break #sortie de la boucle si la conversation marche
        except ValueError:
            print("Erreur : Entrer une valeur valide!")
    r=u
    #vérifier si u pair ou impair
    u=u%2
    #donner le résultat
    if u==1 :
        print(r, "est impair")
    else :
        print(r, "est pair")
#continuer ou pas
    c=input("voulez-vous continuer ? (o=oui - n=non) ").strip().lower()
print("Au revoir")