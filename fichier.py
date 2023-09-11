
def convert_fichier_to_graphe(fichier):
    Liste_sommet = open(fichier,"r",encoding="utf-8").readlines()
    D = {}
    #on convertie le fichier Graph.dan sous forme de liste de dictionnaire avec en clé un sommet et en valeur de clé une liste des voisins
    #Le fichier se trouve sous la forme : Sommet + Chaine de voisin
    #ex : si le sommet A a pour voisin B et K, on écrira ; ABK

    for i in range(len(Liste_sommet)):
        Sommet = Liste_sommet[i].replace("\n","")
        Sommet_actuel = Sommet[0]
        D[Sommet_actuel] = []
        for j in range(1,len(Sommet)):
            D[Sommet[0]].append(Sommet[j])

    return D

def get_all_color():
    #on liste les couleurs depuis le fichier couleur.dan
    Liste_couleur= open("couleur.dan","r",encoding="utf-8").readlines()
    for i in range(len(Liste_couleur)):
        Liste_couleur[i] = Liste_couleur[i].replace("\n","")
    return Liste_couleur


