class Node:
  def __init__(self,cle,valeur, left=None, right=None):
    self.valeur = valeur
    self.cle=cle
    self.left = left
    self.right = right
  def __str__(self) -> str:
      return self.valeur  

def inserer_arbre_rec(noeud:Node, d):
    n = Node(d[0],d[1])
    if noeud == None :
        return n

    if noeud.left == None :
        noeud.left = n
        return noeud  
    else :
        if noeud.right == None :
            noeud.right = n
            return noeud
    inserer_arbre_rec(noeud.left, d)
    inserer_arbre_rec(noeud.right, d)


def afficherArbre(arbre): #affichage du noeud en utilisant le parcours en profondeur 
    file = []
    file.append(arbre)
    parcours = []
    while len(file) > 0:
        parcours.append(file[0].cle)
        sous_arbre = file.pop(0)
        if not sous_arbre.left == None:
            file.append(sous_arbre.left)
        if not sous_arbre.right == None:
            file.append(sous_arbre.right)
    return parcours

def recherhe(abr:Node,k):
    mot=[]
    if abr == None:
        pass
    elif abr.cle ==k:
        print (abr.valeur   , end=" ")
    elif abr.cle !=k :
        recherhe(abr.left,k)
        recherhe(abr.right,k)

dict_french2eng = {"hello" : "bonjour", 
                    "how"   : "comment",
                    "why"   : "pourquoi",
                    "where" :   "ou",
                    "night" :  "nuit",
                    "yes"   : "oui",
                    "no"    : "non",
                    'person' : 'personne',
                    'year' : 'année',
                    'way' : 'moyen',
                    'day' : 'jour',
                    'thing' : 'chose',
                    'man' : 'homme',
                    "world" : 'monde',
                    "life" : 'vie',
                    'hand' : 'main',
                    'part' : 'partie',
                    'child' : 'enfant',
                    'be' : 'être',
                    'have' : 'avoir',
                    'do' : 'faire',
                    'say' : 'dire',
                    'get' : 'obtenir',
                    'make' : 'faire',
                    'go' : 'aller',
                    'know' : 'savoir',
                    'look' : 'regarder',
                    'want' : 'vouloir',
                    'give' : 'donner',
                    'use' : 'utiliser',
                    'find' : 'trouver',
                    'tell' : 'dire à',
                    'ask' : 'demander',
                    'work' : 'travailler',
                    'seem' : 'sembler',
                    'feel' : 'sentir',
                    'try' : 'essayer'}  

# tab = []
# for l in dict_french2eng.items() :
#     tab.append(l)

# tree = Node("x","x")

# for  word in dict_french2eng.items():
#     inserer_arbre_rec(tree, word)

  
# racine
tree = Node('root',['racine']) #The root node of our binary tree

# niveau 1
tree.left = Node('morning',['matin'])
tree.right = Node("world",['monde',])

# niveau 2
tree.left.left = Node("why",['pourquoi'])
tree.left.right = Node("you",['toi','vous'])
tree.right.left = Node("hello",['bonjour'])
tree.right.right = Node("say",['dire'])

# print(tree)





def traduction(x):
    x= x.split(' ')
    for i in range(len(x)):
        recherhe(tree,x[i])
    print("")
        
# print(afficherArbre(tree))
traduction('why say hello world')