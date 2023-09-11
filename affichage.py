import matplotlib.pyplot as plt
import networkx as nx
from numpy import array
from fonction import *



def ajouter_sommet(Graphe,G,dico_couleur):
    """afin d'ajouter les sommets au graph, on liste les sommet et on ajoute des node (c'est a dire des points) a notre figure correspondant au sommet. Ils ont chacun pour
    indice un numéro (ici le compteur de boucle i), un label (le signe du sommet, ici une lettre de l'alphabet) et une couleur préalablement calculer par notre algorithme qui
    retourne un dictionnaire de couleur avec en clé les sommets et en valeur de clé les couleurs de ces sommets."""
    Liste_sommet = list(Graphe.keys())
    for i in range(len(Liste_sommet)):
        sommet = Liste_sommet[i]
        G.add_node(i, label=sommet, col=dico_couleur[sommet])

    """une fois les sommets ajoutés, on les reparcours afin de lister leurs voisins et d'ajouter entre les sommets et leurs voisins des edges, c'est a dire des liaisons"""
    for i in range(len(Liste_sommet)):
        sommet = Liste_sommet[i]
        Liste_voisin = get_voisin(sommet,Graphe)
        for j in range(len(Liste_voisin)):
            G.add_edge(i, Liste_sommet.index(Liste_voisin[j]), weight=6, styl='solid')

def modeliser_graphe(Graphe,Dico_couleur,name):
    """Pour modeliser le graph, on utilise la librairie matplotlib
    On créer la figure avec G = nx.Graph()
     on ajoute ensuite tout les sommets et leurs liaisons grâce a la fonction ajouter_sommet()
     On créer ensuite une liste de couple (sommet,couleur_du_sommet) que l'on retranscrit sous forme de dictionnaire avec
     en clé le sommet et en valeur de clé la couleur du sommet
     La deuxieme liste sert a créer un dictionnaire avec pour clé les indices des sommets et pour valeur de clé les sommets correspondants"""
    G = nx.Graph()
    ajouter_sommet(Graphe,G,Dico_couleur)
    liste = list(G.nodes(data='col'))
    colorNodes = {}
    for noeud in liste:
        colorNodes[noeud[0]]=noeud[1]

    colorList=[colorNodes[node] for node in colorNodes]

    liste = list(G.nodes(data='label'))
    labels_nodes = {}
    for noeud in liste:
        labels_nodes[noeud[0]]=noeud[1]



    #Placement des sommets dans le graph
    pos = nx.spring_layout(G)

    # Ici, on place les points en fonction de leurs positions attribués, leurs tailles (900 pixels), leurs couleurs grace a la liste des couleurs et l'alpha correspondant a la transparence
    nx.draw_networkx_nodes(G, pos, node_size=900, node_color=colorList, alpha=1)

    # Ici on inscrit les lettres correspondant au sommet sur les points précedemment tracé
    nx.draw_networkx_labels(G, pos, labels=labels_nodes,font_size=25 ,font_color='black',font_family='sans-serif')

    # Tout comme les sommets, on trace les arrête les reliants
    nx.draw_networkx_edges(G, pos, width=1)

    #les axes abssices et ordonnées sont enlevé car on ne souhaite pas tracer de courbe
    plt.axis('off')
    #sauvegarde de la figure dans le fichier prévu a cette effet
    plt.savefig("Figure/" + name)
    #fin de la modelisation, on ferme la figure pour eviter que les autres figures se superposent sur celle-ci
    plt.close()

def affichage_depart():
    #affichage de départ
    print("""
 ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗     ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗     ██████╗ ██████╗  ██████╗ ██████╗ ██╗     ███████╗███╗   ███╗    ██╗
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║  ██║    ██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║     ██╔════╝████╗ ████║    ██║
██║  ███╗██████╔╝███████║██████╔╝███████║    ██║     ██║   ██║██║     ██║   ██║██████╔╝██║██╔██╗ ██║██║  ███╗    ██████╔╝██████╔╝██║   ██║██████╔╝██║     █████╗  ██╔████╔██║    ██║
██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══██║    ██║     ██║   ██║██║     ██║   ██║██╔══██╗██║██║╚██╗██║██║   ██║    ██╔═══╝ ██╔══██╗██║   ██║██╔══██╗██║     ██╔══╝  ██║╚██╔╝██║    ╚═╝
╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║    ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║██║██║ ╚████║╚██████╔╝    ██║     ██║  ██║╚██████╔╝██████╔╝███████╗███████╗██║ ╚═╝ ██║    ██╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝    ╚═╝""")
    print("Bienvenue dans ce programmme résolvant le problème de coloriage de graphe !")
    print()
