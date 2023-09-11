import os
from affichage import *
from fichier import *
from fonction_detailled import *

option = "1"

affichage_depart()
while option != "3":
    option = saisie("1 - Résoudre le problème sur un graphe\n2 - Tutoriel\n3 - Sortir du programme\n",["1","2","3"],str)
    if option == "1": #Résoudre le probleme sur un graph
        print()
        option = saisie("1 - Résoudre le problème sur un graph depuis le fichier Graphe.dan\n2 - Résoudre le problème sur un graph généré\n3 - Résoudre le problème sur un graph entré\n",["1", "2", "3"], str)
        Mode = saisie("1 - Résoudre le problème de décidabilité\n2 - Résoudre le problème de calculabilité\n",["1", "2"], str)

        if option == "1": #Résoudre le probleme sur un graph depuis le fichier Graphe.dan
            G = convert_fichier_to_graphe("Graphe.dan")
        elif option == "2": #Résoudre le probleme sur un graph depuis un graph généré
            G = generer_graphe()
        else:
            G = creer_graph()


        if verifier_validite_graph(G) == True: #On peut résoudre le probleme
            if Mode == "1": #Décidabilité
                k = entrer_nombre_positif("Avec combien de couleur voulez vous vérifier la possibilité de colorier le graph ? ")
                Coloriage_possible,Liste_des_couleurs,configuration_des_couleurs = resoudre_probleme_coloriage(G,Mode,k)
                if Coloriage_possible:
                    print("Réponse : Il est possible de colorier le Graph donné à l'aide de " + str(k) + " couleurs")
                else:
                    print("Réponse : Il est impossible de colorier le Graph donné à l'aide de " + str(k) + " couleurs")


            else:
                Nombre_couleur,Liste_des_couleurs,configuration_des_couleurs = resoudre_probleme_coloriage(G, Mode)
                print("Le nombre minimal de couleur pour dessiner le graph donné est " + str(Nombre_couleur))

            print()
            option = saisie("Souhaitez vous réaliser une modélisation du graph dessiné avec un nombre de couleur minimal ?",["oui","non"], str)
            if option == "oui":
                name = saisie("Entrez un nom pour l'image du graph ",None, str)
                modeliser_graphe(G,configuration_des_couleurs,name)
                print("Graph modélisé ! Le fichier apparaitra après la fermeture du programme")


        else:
            print()
            print("Le graph entré est invalide ! Afin de créer un graph correctement, consultez le tutoriel")
            option = "1"
        print()

    elif option == "2":
        question = ""
        #on liste les question grace au fichier tutoriel qui contient des txt avec les réponses dont les questions sont les noms des fichiers
        #L'option choisie est convertie en int et sert d'indice a la liste des tutoriels afin d'ouvrir le bon fichier et d'afficher la réponse
        Liste_question = os.listdir("tutoriel/")
        for i in range(len(Liste_question)):
            question += str(i+1) + " - " + Liste_question[i].replace(".txt","") + "\n"

        option_question = saisie(question,[i+1 for i in range(len(Liste_question))], int)
        print(open("tutoriel/" + Liste_question[option_question-1],"r",encoding="utf-8").read())
        print()







