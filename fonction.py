#Structure utilisé : dictionnaire de liste
import copy
import random
import time

from fichier import *

def saisie(affichage,condition_stop,type_of_input):
    #fonction de saisie prenant en paramères :
    #affichage : affiche la question posé a l'utilisateur avant les choix
    #condition stop : liste des réponses possible OU None si la réponse n'est pas importante
    #type of input : types de notre input que l'on veux

    print(affichage,end="")
    #si il n'y aucune "limite" dans les réponses possibles, on renvoie juste un input de ce que souhaite le joueur
    if condition_stop == None:
        return input("")
    else:
        #Si il y a une limite de réponse, on affiche toutes les réponse entre parenthèse
        print(" (",end="")
        for i in range(len(condition_stop)):
            if i!= len(condition_stop)-1:
                print(condition_stop[i], end="/")
            else:
                print(condition_stop[i], end=") ")
        Saisie = "$$$"
        #la boucle va se repeter tant qu'on obtient pas une des réponses souhaitées
        while Saisie not in condition_stop:
            try:
                #le try es utile pour deux choses :
                #1 - si l'utilisateur entre une chaine de caractere alors qu'on souhaite un autre type, la saisie ne s'arrête pas
                #2 - la provocation d'erreur pour verifier si une réponse souhaité est entrée permet de ré-afficher la question
                #cela evite d'avoir un espace vide pour le input

                Saisie = type_of_input(input(""))
                assert Saisie in condition_stop
            except:
                #ré affichage de la question en cas de problème
                print(affichage,end=" (")
                for i in range(len(condition_stop)):
                    if i != len(condition_stop) - 1:
                        print(condition_stop[i], end="/")
                    else:
                        print(condition_stop[i], end=") ")
        return Saisie

def chaine_to_dico(chaine,L_sommet):
    """Cette fonction a pour but de retourner un dicctionnaire de la combinaison de couleur créer dans tester_possibilite depuis la chaine de caractere donné
    Pour cela, on créer une Liste a partire de la chaine de la forme :
    couleur1
    couleur2
    ...
    couleurn (avec n le nombre de sommets du graph)
    Ensuite, on assigne chaque couleur a un sommet
    Puisque toutes les possibilités de combinaisons de couleur seront testé, on aura toutes les possibilités d'association aux sommets"""


    Dico = {}
    #création du dictionnaire retourné
    L_text_chaine = chaine.split("\n")[1:]
    for i in range(len(L_sommet)):
        Dico[L_sommet[i]] = L_text_chaine[i]
    return Dico

def get_voisin(sommet,Graphe):
    #retourne la liste des voisins
    return Graphe[sommet]

def generer_graphe():
    nb_sommet = random.randint(3,4)
    Alphabet = ""
    Graphe = {}
    for i in range(nb_sommet):
        Alphabet += chr(65+i)
        Graphe[Alphabet[i]] = []

    for i in range(len(Alphabet)):
        sommet_parcourue = Alphabet[i]
        for j in range(len(Alphabet)):
            voisin_potentielle = Alphabet[j]
            if random.random() < random.random() and voisin_potentielle not in Graphe[sommet_parcourue] and voisin_potentielle != sommet_parcourue:
                Graphe[sommet_parcourue].append(voisin_potentielle)
                Graphe[voisin_potentielle].append(sommet_parcourue)
                Graphe[sommet_parcourue].sort()
                Graphe[voisin_potentielle].sort()

    return Graphe


#Fonction Brut force


def verifier_graph_couleur_valide(Graph,L_sommet,dico_couleur):
    """Pour verifier si un graphe a une configuration de couleur valide, on va parcourire chaque sommet et vérifier si leurs voisins ont une couleur identique à la leur.
    Si c'est bien le cas et que les deux sommets sont distincts, alors la fonction return False. Si la configuration est validé, alors la fonction retournera True en sortie de la double boucle """
    for i in range(len(L_sommet)):
        for j in range(len(L_sommet)):
            if i != j and L_sommet[i] in get_voisin(L_sommet[j],Graph) and dico_couleur[L_sommet[j]] == dico_couleur[L_sommet[i]]:
                return False
    return True

def tester_possibilite(chaine,nb_sommet,L_sommet,L_couleur,L_P):
    """Afin de tester toutes les possibilité, on utilise la méthode reccursif :
    Tout comme pour un arbre de probabilité, on va venir tester tout les chemins existant parmis les possibilités de couleurs n fois (avec n le nombre de sommet du graph)
    Par exemple, si le graphe possède 3 sommets et qu'on possède deux couleurs la fonction grâce a la boucle va effectuer les chemins suivant ;

                        bleu | chemin de sortie : bleu-bleu-bleu
              1.1) bleu ---
                        rouge | chemin de sortie : bleu-bleu-rouge
    1) bleu ---
                        bleu | chemin de sortie : bleu-rouge-bleu
              1.2) rouge ---
                        rouge | chemin de sortie : bleu-rouge-rouge

                        bleu | chemin de sortie : rouge-bleu-bleu
              2.1) bleu ---
                        rouge | chemin de sortie : rouge-bleu-rouge

    2) rouge ---
                        bleu | chemin de sortie : rouge-rouge-bleu
              2.2) rouge ---
                        rouge | chemin de sortie : rouge-rouge-rouge

    On va donc imbriquer des boucles a chaque sommet en plus
    Ici, on a trois boucle car on teste toutes les combinaisons possibles d'un ensemble a 2 possibilité avec 3 elements
    La réccursivité permet ainsi d'emboiter des boucles.
    Afin de savoir lorsqu'on arrive au cas de base, on fait décroitre une valeur correspondant au départ au nombre de sommet
    Lorsque cette valeur atteint 1, on sait qu'on arrive au cas de base car il ne reste qu'une boucle
    Pendant l'appel réccursif, on utilise une variable de type str permettant de sauvegarder le chemin parcourue (par exemple,
    durant le deuxieme tout de boucle 1.2, notre string sera bleu\nrouge
    Quand la fonction atteint le cas de base, on construit le dictionnaire à partir de notre chaine décrivant le chemin finale, et on l'ajoute a une liste des possibilités
    que nous parcourerons ensuite pour tester la validité de ceux-ci.
    On vérifie que le dictionnaire n'est pas dans la liste afin d'éviter les répetitions
    """



    if nb_sommet != 1:
        for i in range(len(L_couleur)):
            tester_possibilite(chaine + "\n"  + L_couleur[i] ,nb_sommet-1,L_sommet,L_couleur,L_P)
    else:
        for i in range(len(L_couleur)):
            Dico = chaine_to_dico(chaine + "\n"  + L_couleur[i],L_sommet )
            if Dico not in L_P:
                L_P.append(Dico)

def calculer_nombre_couleur_minimum_Graph(Graph):
    """List_couleur : liste des couleurs obtenue depuis le fichier couleur.dan, utile pour modéliser le graph
       nombre_couleur_test : compteur du nombre de couleur necessaire pour dessiner le graph
       On continue de chercher le nombre de couleur minimal pour résoudre le problème à l'infinis grâce a la boucle while
       On modifie la liste des couleurs utilisé (L_couleur) en y mettant le nombre de couleur que l'on test.
       On vide la liste des possibilités afin de ne pas retester les configurations antérieur
       On teste ensuite toutes les possibilités de chemins de couleur ce qui remplis la liste des possibilités de configurations
       Une fois cela fait, on verifie la validité de toute les configurations dans la liste des possibilités grâce a la fonction verifier_graph_couleur_valide
       Si une configuration valide est trouvé, on return la liste des couleurs et le dictionnaire de la configuration validé des couleurs
       Si aucune configuration n'est trouvée, on rajoute une couleur et on recommence
    """
    Liste_couleur = get_all_color()
    nombre_couleur_test = 1
    L_sommet = list(Graph.keys())
    while True:
        L_couleur = Liste_couleur[:nombre_couleur_test]
        L_possibilite = []
        nb_sommet = len(L_sommet)
        tester_possibilite("",nb_sommet,L_sommet,L_couleur,L_possibilite )
        for i in range(len(L_possibilite)):
            if verifier_graph_couleur_valide(Graph,L_sommet,L_possibilite[i]) == True:
                return (L_couleur,L_possibilite[i])
        nombre_couleur_test += 1

def resoudre_probleme_coloriage(Graph,Mode,k=None):
    """En utilisant la liste de couleur et le dictionnaire de couleurs renvoyer par la fonction calculer_nombre_couleur_minimum_Graph, on peut résoudre le
    problème sous sa forme décidabilité et calculabilité
    Si la forme est décidabilité (correspond a 1), on vérifie que le nombre de couleur minimal necessaire au coloriage du graph est inférieur ou égale à l'entier k donnée, la liste de couleur et la configuration valide
    Si la forme est calculabilité, alors on retournera simplement le nombre de couleur minimal necessaire au coloriage du graph, la liste de couleur et la configuration valide """

    L_couleur, dico_couleur = calculer_nombre_couleur_minimum_Graph(Graph)
    if Mode == "1": #décidabilité
        return (len(L_couleur)  <= k,L_couleur, dico_couleur)
    else: #calculabilité
        return (len(L_couleur),L_couleur, dico_couleur)

#fonction supplémentaire

def verifier_validite_graph(G):
    """cette fonction est utilisé pour vérifier que l'utilisateur n'entre pas un graph orienté en vérifiant que si un sommet possède un vosin, ce voisin possède bien
    pour voisin le sommet évoqué precedemment
    La fonction retourn False dès que celle ci détecte une erreur. Si aucune erreur n'est détécté, la fonction return True"""
    for sommet in G:
        Liste_voisin_sommet = get_voisin(sommet,G)
        for i in range(len(Liste_voisin_sommet)):
            voisin = Liste_voisin_sommet[i]
            if sommet not in get_voisin(voisin,G) :
                return False
    return True

def entrer_nombre_positif(affichage):
    """fonction de saisie d'un nombre positif empechant une erreur d'arriver retournant ce nombre"""
    k = -1
    while k < 0:
        try:
            k = int(input(affichage))
        except:
            k = -1
    return k

def creer_graph():
    G = {}
    """La fonction ici sert pour créer un graph entré, on demande d'abord le nombre de sommet puis on se sert de l'alphabet afin de construire les sommets
    pour chaque sommets, on demande les voisins et on entre ceux-ci en chaine. Ensuite, on parcours chaque sommets voisins puis on les ajoutes a la liste des voisins 
    du sommet.
    La structure retourné est un dictionnaire de liste"""
    nb_sommet = entrer_nombre_positif("nombre de sommet du graph ")
    for i in range(nb_sommet):
        Sommet = chr(65+i)
        G[Sommet] = []
        Voisin = input("entrez les voisins du sommet " + Sommet +" ")
        for j in range(len(Voisin)):
            G[Sommet].append(Voisin[j])
    return G

