##-----Importation des Modules-----##

from tkinter import *
from random import *
from copy import *

##-----Définition des Variables globales-----##

lignes = 40          # Nombre de lignes du tableau                               
colonnes = 70        # Nombre de colonnes du tableau                                
d = 15               

cellules = []  
grille = []  
cell_rapide = []
pourcentcellule = 0     # Initialisation du proucentage de cellules en vie au départ
nbgen = 0               # Initialisation du nombre de générations
nbcell = 0              # Initialisation du nombre de cellules vivantes au départ
drapeau = True          # Au départ, drapeau True c'est à dire que le jeu est en pause

##-----Définitions des Fonctions-----##


def aleatoire():                # Défintion d'une fonction aléatoire 
    
    global cellules, grille, lignes, colonnes, d , cell_rapide , drapeau , nbgen , pourcentcellule , nbcell # Enonciation des variables globales
    
    dessin.delete(ALL)          # On supprime tout ce qui a été précedemment déssiné                                                                                             
    cellules = []               # On crée deux listes qui se rempliront de coordonnées des cellules                             
    grille = []
    cell_rapide = []            # On crée également une liste "rapide" qui permettra de faciliter les tests que l'on fera subir aux listes
    
    drapeau = True              # Le jeu est en pause
    
    nbgen = 0                   # Le nombre de générations est remis à zéro
    
    for i in range(lignes):     # Pour chaque ligne ...                            

        cellules.append([])     # On ajoute aux listes cellules et grille des autres listes qui correspondront aux coordonnées de chaque cellule
        grille.append([])                                            

        for j in range(colonnes):   #...et chaque colonne
            
            chance_cellule = random()   # On fait subir à chaque cellule un aléa désigné par la variable chance_cellule qui contient un nombre décimal aléatoire compris entre 0 et 1 (inclus)            
            if chance_cellule <= pourcentcellule/100 :    # Si ce nombre est inférieur ou égal au pourcentage divisé par cent choisi par l'utilisateur,..
                
                grille[i].append(dessin.create_rectangle(2+j*d, 2+i*d, 2+(j+1)*d, 2+(i+1)*d, outline='#FF508C', fill='#FF508C'))    # On remplit cette cellule comme une cellule en vie
                cellules[i].append(1)   #..et on lui donne le chiffre 1 symbolisant le fait qu'elle est en vie par opposition au zéro signifiant que la cellule est morte
            else:                       # Si le nombre est strictement supérieur au pourcentage divisé par cent choisi par l'utilisateur,..
                grille[i].append(dessin.create_rectangle(2+j*d, 2+i*d, 2+(j+1)*d, 2+(i+1)*d, outline='#EEEEEE', fill='#FFFFFF'))    # On remplit cette cellule comme une cellule morte
                cellules[i].append(0)   #..et on lui donne le chiffre 0
                
    maj()             # On appelle ensuite la fonction maj qui sert de fonction graphique et qui va compter le nombre de cellules actuellement en vie
    
    cell_rapide = deepcopy(cellules)    # On crée une copie de la liste des cellules ainsi obtenues
    
    gen.configure(text="Générations : " + str(nbgen)) # On met à jour le nombre de générations affichées
    bouton_pause.configure(text='Commencer')          # On met à jour le bouton pause pour qu'à la place de 'pause' il affiche 'Commencer'
    pourcent.configure(text='Pourcentage de cellules moyen : ' + str(pourcentcellule) + ' %') # On met à jour le pourcentage de cellules en vies affiché


def moins():    # On définit l'action que l'on va attribuer au bouton moins
    
    global pourcentcellule  # On rend la variable utilisée dans la fonction globale
    
    if pourcentcellule > 0:     # Si la valeur est supérieure à zéro..
        pourcentcellule -= 5    # ..on lui soustrait 5
    else:       # Si la valeur est inférieure ou égale à zéro
        pourcentcellule = 0     # Cette valeur reste zéro (Pour empêcher le pourcentage d'être négatif)
    pourcent.configure(text='Pourcentage de cellules moyen : ' + str(pourcentcellule) + ' %')     # Enfin, on met à jour l'affichage de pourcentage de cellules vivantes
    

def plus():     # On définit l'action que l'on va attribuer au bouton plus
    
    global pourcentcellule  # On rend la variable utilisée dans la fonction globale  
    
    if pourcentcellule < 100:   # Si la valeur est inférieure à cent..
        pourcentcellule += 5    # ..on lui ajoute 5
    else:      # Si la valeur est supérieure ou égale à cent
        pourcentcellule = 100   # Cette valeur reste cent (Pour empêcher le pourcentage d'être supérieur à 100%) 
    pourcent.configure(text='Pourcentage de cellules moyen : ' + str(pourcentcellule) + ' %')     # Enfin, on met à jour l'affichage de pourcentage de cellules vivantes
    

def pause():    # On définit la fonction du bouton qui va permettre au jeu de se figer
    
    global drapeau      # On rend la variable utilisée dans la fonction globale  
    
    if drapeau == False:    # Si le jeu n'est pas en pause,
        drapeau = True      # le bouton fige le jeu
        bouton_pause.configure(text='Continuer')    #..et il est également renommé Continuer
    elif drapeau == True:   # Si le jeu est en pause,
        drapeau = False     # le bouton relance l'action
        bouton_pause.configure(text='Pause')        #.. et il est également renommé Pause


def automate(): # On définit le programme principal du jeu
    
    global cellules, grille, lignes, colonnes, d , cell_rapide , drapeau , nbgen , pourcentcellule , nbcell, listmem # On rend les variables utilisées dans la fonction globales  
     
    dessin.delete(ALL)      # On supprime tout ce qui a pu être précedemment utilisé                                                                                              
    cellules = []           # On crée deux listes qui se rempliront de coordonnées des cellules                            
    grille = []             
    cell_rapide = []        # On crée également une liste "rapide" qui permettra de faciliter les tests que l'on fera subir aux listes
    listmem = []
    
    drapeau = True          # Le déroulement de l'action est en pause
    
    nbgen = 0               # Le nombre de générations est remis à zéro
    nbcell = 0              # Le nombre de cellules en vie est remis à zéro également

    pourcentcellule = 15    # On a initialement 15% de chance de générer une cellule vivante pour chaque case du tableau
    
    for i in range(lignes): # Pour chaque ligne ...           
        
        cellules.append([]) # On ajoute aux listes cellules et grille des autres listes qui correspondront aux coordonnées de chaque cellule
        grille.append([])
        
        for j in range(colonnes):    #...et chaque colonne
            grille[i].append(dessin.create_rectangle(2+j*d, 2+i*d, 2+(j+1)*d, 2+(i+1)*d, outline='#EEEEEE', fill='#FFFFFF'))     # On remplit cette cellule comme une cellule morte
            cellules[i].append(0)    #..et on lui donne le chiffre 0
            
    cell_rapide = deepcopy(cellules)    # On crée une copie de la liste des cellules ainsi obtenues
    if nbgen % 2 != 0 :                 # Si le nombre de génération est impair
        listmem = deepcopy(cell_rapide)     # On mémorise dans une autre liste les cellules en vies pour les générations impaires
    
    fen.after(50,idee_de_sami) # On réapplique la fonction idee_de_sami toutes les 50 millisecondes
    if listmem == cellules :        # Si les cellules en vies sont les mêmes que celles d'il y a deux générations,
        drapeau = False             # Alors on met le jeu en marche
        texte4.configure(text="Jeu mis sur pause car présence uniquement de figures stables") # Et l'on affiche que les figures présentes sont toutes stables
    else :
        gen.configure(text="Générations : " + str(nbgen))   # On met à jour le nombre de générations effectuées affiché
    bouton_pause.configure(text='Commencer')    # Le bouton Pause est renommé en bouton Commencer
    pourcent.configure(text='Pourcentage de cellules moyen : ' + str(pourcentcellule) + ' %') # On met à jour le pourcentage de chance de vie des cellules
    cell.configure(text="Cellules vivantes : " + str(nbcell))   # On met à jour le nombre de cellules actuellement vivantes affiché
    

def restart():  # On défnit la fonction permettant de relancer le jeu
    
    global cellules, grille, lignes, colonnes, d , cell_rapide , drapeau , nbgen , pourcentcellule , nbcell # On rend les variables utilisées dans la fonction globales  
     
    dessin.delete(ALL)   # On supprime tout ce qui a pu être précedemment utilisé                                                                                                     
    cellules = []        # On crée deux listes qui se rempliront de coordonnées des cellules                                 
    grille = []
    cell_rapide = []     # On crée également une liste "rapide" qui permettra de faciliter les tests que l'on fera subir aux listes
    
    drapeau = True       # Le déroulement de l'action est en pause
    
    nbgen = 0            # Le nombre de générations est remis à zéro
    nbcell = 0           # Le nombre de cellules en vie est remis à zéro également
    
    for i in range(lignes): # Pour chaque ligne ...
        
        cellules.append([]) # On ajoute aux listes cellules et grille des autres listes qui correspondront aux coordonnées de chaque cellule
        grille.append([])
        
        for j in range(colonnes):    #...et chaque colonne
            grille[i].append(dessin.create_rectangle(2+j*d, 2+i*d, 2+(j+1)*d, 2+(i+1)*d, outline='#EEEEEE', fill='#FFFFFF'))    # On remplit cette cellule comme une cellule morte
            cellules[i].append(0)    #..et on lui donne le chiffre 0
            
    cell_rapide = deepcopy(cellules) # On crée une copie de la liste des cellules ainsi obtenues
    gen.configure(text="Générations : " + str(nbgen))    # On met à jour le nombre de générations effectuées affiché
    bouton_pause.configure(text='Commencer')    # On met à jour le bouton pause pour qu'à la place de 'pause' il affiche 'Commencer'
    pourcent.configure(text='Pourcentage de cellules moyen : ' + str(pourcentcellule) + ' %') # On met à jour le pourcentage de chance de vie des cellules
    cell.configure(text="Cellules vivantes : " + str(nbcell))    # On met à jour le nombre de cellules actuellement vivantes affiché


def vie(i,j):   # On définit la fonction qui va permettre de connaître les conditions de vie de la cellule à la prochaine génération
    
    global cellules, lignes, colonnes , cell_rapide # On rend les variables utilisées dans la fonction globales  
    
    nb_voisines = voisines(i,j) # On compte combien il y a de cases vivantes dans le voisinage de la cellule
    
    if cellules[i][j] == 0 and nb_voisines == 3 :       # Si la cellule est morte et qu'elle a exactement 3 cellules en vie dans son voisinage,
        cell_rapide[i][j] = 1                           # ..alors elle devient vivante à la prochaine génération
    elif cellules[i][j] == 1 and nb_voisines <= 1 :     # Si la cellule est en vie et a une cellule vivante ou moins  dans son voisinage,
        cell_rapide[i][j] = 0                           # ..alors elle meurt à la prochaine génération
    elif cellules[i][j] == 1 and nb_voisines >= 4 :     # Si la cellule est en vie et a au moins 4 cellules en vie dans son voisinage,
        cell_rapide[i][j] = 0                           # ..alors elle meurt à la prochaine génération

    
    
def maj():
    
    global cellules, lignes, colonnes , cell_rapide , nbcell        # fonction graphique
    
    nbcell = 0
    
    for i in range (lignes) :                                       # Pour chaque ligne
        for j in range(colonnes) :                                  # ..et chaque colonne
            
            verif = cellules[i][j]                                  # On attribue le contenu de la cellule étudiée dans une variable 'verif'
            
            if verif == 1 :                                         # Si cette cellule est en vie
                dessin.itemconfigure(grille[i][j], fill='#FF508C',outline='#FF508C')    # Alors on la colore en rose            
            else:                                                   # Sinon
                dessin.itemconfigure(grille[i][j], fill='#FFFFFF',outline='#EEEEEE')    # Alors on la colore en blanc
    
    for i in range(lignes):                                         # Pour chaque ligne
        nbcell += cellules[i].count(1)                              # On compte le nombre de cellules vivantes ainsi comptées
    
    cell.configure(text="Cellules vivantes : " + str(nbcell))       # Et on met à jour l'affichage pour l'utilisateur

def action(event):  # Fonction utilisée par le clavier pour passer une unique génération
    
    global cellules, lignes, colonnes , cell_rapide , nbgen
    
    for i in range(lignes):                                     # Pour chaque ligne                                                                
        for j in range(colonnes):                               # et chaque colonne
            vie(i,j)                                            # On applique la fonction vie à la cellule
    cellules = deepcopy(cell_rapide)                            # On copie à l'identique la liste de cellules analysées
    maj()                                                       # On fait appel à la fonction graphique
    nbgen += 1                                                  # On augmente le nombre de générations ainsi réalisés
    gen.configure(text="Générations : " + str(nbgen))           # On met à jour l'affichage du nombre de générations pour l'utilisateur
    
def click(event):   # On définit l'évènement 'clic de l'utilisateur'
    
    global d , cellules , cell_rapide , lignes , colonnes   # On rend les variables utilisées dans la fonction globales  
    
    j = (event.x-2)//d  # Colonne du clic   
    i = (event.y-2)//d  # Ligne du clic
    
    verif = cellules[i][j] 
    
    if verif == 0:      # Si la cellule vérifiée est morte
        cellules[i][j] = 1# elle deviens vivante
    elif verif == 1:    # Si la cellule vérifiée est vivante
        cellules[i][j] = 0  # elle meurt
    
    cell_rapide[i][j] = cellules[i][j]
    maj()
    
def idee_de_sami():
    
    global cellules, lignes, colonnes , cell_rapide , nbgen , drapeau #'argumentation'
    
    
    
    if drapeau == False:                                    # Si le jeu est en marche
        for i in range(lignes):                             # Pour chaque ligne                                                                            
            for j in range(colonnes):                       # Et pour chaque colonne
                vie(i,j)                                    # On fait appel à la fonction qui va permettre de connaître les conditions de vie de la cellule à la prochaine génération   
        cellules = deepcopy(cell_rapide)                    # On copie à l'identique la liste de cellules analysées
        maj()                                               # On fait appel à la fonction graphique
        nbgen += 1                                          # On augmente le nombre de générations ainsi réalisés
        gen.configure(text="Générations : " + str(nbgen))   # On met à jour l'affichage du nombre de générations pour l'utilisateur
    fen.after(50,idee_de_sami)                              # On relance cette fonction toutes les 50 millisecondes

def voisines(i, j):     # On définit une fonction qui renvoie le nombre de cases en vie autour d'une cellule [i][j], on fait une liste exhaustive des cas particuliers
    
    global cellules, lignes, colonnes     # On rend les variables utilisées dans la fonction globales  
    
    liste=[]                              # On crée une liste vide        
    
    if i == 0 and j == 0 :                # Si la cellule est dans le coin supérieur gauche du tableau               
        liste = [cellules[i][j+1],cellules[i+1][j],cellules[i+1][j+1]]
    elif i == 39 and j == 0 :             # Si la cellule est dans le coin supérieur droit
        liste = [cellules[i-1][j],cellules[i-1][j+1],cellules[i][j+1]]
    elif i == 0 and j == 69 :             # Si la cellule est dans le coin inférieur gauche du tableau
        liste = [cellules[i][j-1],cellules[i+1][j-1],cellules[i+1][j]]
    elif i == 39 and j == 69 :            # Si la cellule est dans le coin inférieur droit
        liste = [cellules[i-1][j-1],cellules[i-1][j],cellules[i][j-1]]
    elif i == 0 and j > 0 and j < 69 :    # Si la cellule est située dans la première ligne du tableau
        liste = [cellules[i][j-1],cellules[i][j+1],cellules[i+1][j-1],cellules[i+1][j],cellules[i+1][j+1]]
    elif i == 39 and j > 0 and j < 69 :   # Si la cellule est située dans la dernière ligne du tableau
        liste = [cellules[i-1][j-1],cellules[i-1][j],cellules[i-1][j+1],cellules[i][j-1],cellules[i][j+1]]
    elif i > 0 and i < 69 and j == 0 :    # Si la cellule est située dans la première colonne du tableau
        liste = [cellules[i-1][j],cellules[i-1][j+1],cellules[i][j+1],cellules[i+1][j],cellules[i+1][j+1]]
    elif i > 0 and i < 39 and j == 69 :   # Si la cellule est située dans la dernière collonne du tableau
        liste = [cellules[i-1][j-1],cellules[i-1][j],cellules[i][j-1],cellules[i+1][j-1],cellules[i+1][j]]
    else :                                # Dans tous les autres cas
        liste = [cellules[i-1][j-1],cellules[i-1][j],cellules[i-1][j+1],cellules[i][j-1],cellules[i][j+1],cellules[i+1][j-1],cellules[i+1][j],cellules[i+1][j+1]]
        
    nb_liste = liste.count(1)             # On compte ensuite le nombre de cellules en vie dans la liste obtenue
    
    return nb_liste                       # Et la fonction renvoie ce nombre

##-----Création de la fenêtre-----##

fen=Tk()                                  # On crée la fenêtre                      
fen.title('Jeu de la vie')                # On la nomme Jeu de la vie           
fen.resizable(width=False, height=False)  # On la rend impossible à être redimensionnée 

##-----Création d'un canevas et d'une grille dans le canevas-----##

dessin=Canvas(fen, bg='#000000', width=d*colonnes+1, height=d*lignes+1) # On crée le canvas  
dessin.grid(row = 0, column = 0 , columnspan=5 , padx = 5 , pady = 5)   # On le décale légèrement pour qu'il soit entièrement visible

##-----Création des boutons-----##

bouton_pause = Button(fen, text='', command=pause)                      # On crée un bouton qui commande la fonction pause
bouton_pause.grid(row = 3, column = 3 , pady = 5)

bouton_restart = Button(fen, text='Recommencer', command=restart)       # On crée un bouton qui commande la fonction restart
bouton_restart.grid(row = 4, column = 3 , pady = 5)

bouton_moins = Button(fen, text='-', command=moins)
bouton_moins.grid(row = 2, column = 0 , rowspan = 2 , sticky = E)       # On crée un bouton qui commande la fonction moins

bouton_plus = Button(fen, text='+', command=plus)                       # On crée un bouton qui commande la fonction plus
bouton_plus.grid(row = 2, column = 2, rowspan = 2 , sticky = W)

bouton_aleatoire = Button(fen, text='Aléatoire', command=aleatoire)     # On crée un bouton qui commande la fonction aleatoire
bouton_aleatoire.grid(row = 3, column = 1)


##-----Création des zones de texte-----##

gen=Label(fen , text="Générations : " + str(nbgen))                             # On crée une zone de texte pour le nombre de générations effectuées par le programme
gen.grid(row=1,column=3)

cell=Label(fen , text="Cellules vivantes : " + str(nbcell))                     # On crée une zone de texte pour indiquer le nombre de cellules actuellement vivantes
cell.grid(row=2,column=3)

texte1=Label(fen , text='COMMANDES :')                                          # On crée une zone de texte pour indiquer quelles sont les commandes puis on les définis ci-dessous
texte1.grid(row=1,column=4)

texte2=Label(fen , text='- Clic Gauche pour ajouter ou retirer une cellule')    
texte2.grid(row=2,column=4)

texte3=Label(fen , text='- Touche du clavier pour passer manuellement une génération')
texte3.grid(row=3,column=4)

texte4=Label(fen, text='')
texte4.grid(row=5,column=3)

pourcent=Label(fen , text='Pourcentage de cellules moyen : ' + str(pourcentcellule) + ' %')   # On affiche le Pourcentage de cellules moyen (par défaut 15)
pourcent.grid(row=1,column=1,rowspan =2)

##-----Programme principal-----##

fen.bind('<Key>', action)               # On associe le fait d'utiliser une touche du clavier à 'action'
dessin.bind('<Button-1>' , click)       # On associe le fait d'effectuer un clic gauche à 'click'
automate()                              # On lance la fonction principale du programme

fen.mainloop()                          # Boucle d'attente des événements                  
try:                                    # Fermeture "correcte" de la fenêtre
    fen.destroy()                                   
except TclError:
    pass 
