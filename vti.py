from PIL import Image
import os
from matplotlib import pyplot as plt
import numpy as np

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)
    
    
    
#___________________________div 3_____________________________________________


def DIV3():
    # On Précise le chemin de notre image
    img = Image.open(r"C:\Users\chateau noir\Desktop\vti\\image.jpg")

    # Remplir la matrice de pixels
    Matrice = img.load()

    # Récuperation de la longeur et la largeur de notre image
    Width = img.width
    Height = img.height


    # Création d'une image
    imgGris= Image.new( img.mode, img.size)

    # Création d'une matrice de pixel pour notre 2e image
    img2 = imgGris.load()

    #On parcours
    for i in range(Width):
        for j in range(Height):
            # On récupère les composantes RVB du pixel
            Rouge = Matrice[i, j][0]
            Vert = Matrice[i, j][1]
            Bleu = Matrice[i, j][2]

            # On calcule notre valeur de gris
            gris =  round((Rouge + Vert + Bleu) / 3)

            img2[i,j] = (gris, gris, gris)
      
   
    #Emplacement de l'image crée
    imgGris.save(r"C:\Users\chateau noir\Desktop\vti\\image_en_div3.jpg")
    
    
    
    #histogramme
    plt.hist(gris, range = (0, 256), bins = 5, color = 'yellow', edgecolor = 'blue')
    plt.xlabel('valeurs')
    plt.ylabel('nombres')
    plt.title('Exemple d\' histogramme simple')
    plt.show()
    
    
    print('')
    print('')

    #Calcul de la taille en bytes (octets)
    print("Taille du fichier en div3 : {} ".format(os.stat(r"C:\Users\chateau noir\Desktop\vti\\image_en_div3.jpg").st_size))
    return imgGris




#___________________________Norme_CIE_709______________________________________



def Norme_CIE_709():
    # On Précise le chemin de notre image
    img = Image.open(r"C:\Users\chateau noir\Desktop\vti\\image.jpg")

    # Remplir la matrice de pixels
    Mat_Pix = img.load()

    # Récuperation de la longeur et la largeur de notre image
    Width = img.width
    Height = img.height

    # Création d'une image
    imgSortie = Image.new( img.mode, img.size)

    # Création d'une matrice de pixel pour notre 2e image
    img2 = imgSortie.load()

    # Parcourir la matrice des pixels
    for i in range(Width):
        for j in range(Height):
            # On récupère les composantes RVB du pixel
            Rouge = Mat_Pix[i, j][0]
            Vert = Mat_Pix[i, j][1]
            Bleu = Mat_Pix[i, j][2]
            # Calcule de la valeur gris
            gris =  round(0.2125 * Rouge + 0.7154 * Vert + 0.0721 * Bleu)

            img2[i, j] = (gris, gris, gris)

    #Emplacement de l'image crée
    imgSortie.save(r"C:\Users\chateau noir\Desktop\vti\\image_CIE_709.jpg")
    
    #HISTOGRAMME
    plt.hist(gris, range = (0, 256), bins = 10, color = 'yellow', edgecolor = 'black')
    plt.xlabel('valeurs')
    plt.ylabel('nombres')
    plt.title('Norme_CIE_709')
    plt.show()
    
    print('')
    print('')

    #Calcul de la taille en bytes (octets)
    print("Taille du fichier en Norme 709  : {} ".format(os.stat(r"C:\Users\chateau noir\Desktop\vti\\image_CIE_709.jpg").st_size))
    return imgSortie




#____________________________Norme_CIE_601_____________________________________



def Norme_CIE_601():
    # On Précise le chemin de notre image
    img = Image.open(r"C:\Users\chateau noir\Desktop\vti\\image.jpg")

    # Remplir la matrice de pixels
    Mat_Pix = img.load()

    # Récuperation de la longeur et la largeur de notre image
    Width = img.width
    Height = img.height

    # Création d'une image
    imgSortie = Image.new( img.mode, img.size)

    # Création d'une matrice de pixel pour notre 2e image
    img2 = imgSortie.load()

    # Parcourir la matrice des pixels
    for i in range(Width):
        for j in range(Height):
            # On récupère les composantes RVB du pixel
            Rouge = Mat_Pix[i, j][0]
            Vert = Mat_Pix[i, j][1]
            Bleu = Mat_Pix[i, j][2]
            # Calcule de la valeur gris
            gris =  round(0.299 * Rouge + 0.587 * Vert + 0.114 * Bleu)

            img2[i, j] = (gris, gris, gris)


    #Emplacement de l'image crée
    imgSortie.save(r"C:\Users\chateau noir\Desktop\vti\\image_CIE_601.jpg")
    
   
    
    
    #histogrm
    plt.hist(gris, range = (0, 256), bins = 20, color = 'yellow', edgecolor = 'red')
    plt.xlabel('valeurs')
    plt.ylabel('nombres')
    plt.title('Norme_CIE_601')
    plt.show()
    
    
    
    print('')
    print('')
    
    
    
    #Calcul de la taille en bytes (octets)
    print("Taille du fichier en Norme 601  : {} ".format(os.stat(r"C:\Users\chateau noir\Desktop\vti\\image_CIE_601.jpg").st_size))
    return imgSortie

#__________________________________huffman__________________________________________________

# Implementation du codage de Huffman
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d
#_______________________________sorie d image_____________________________________________


#appele de fonction pour avoir les images en sortie
image = DIV3()
image601=Norme_CIE_601()
image701=Norme_CIE_709()

#________________________________fonction histogramme_____________________________________


#________________________________partie 2 du travail_______________________________________



img = Image.open(r"C:\Users\chateau noir\Desktop\vti\\image_en_div3.jpg")

# Remplir la matrice de pixels
pixel_mat = img.load()

# Liste des fréqences
freq = {}

# liste des valeurs de niveau de gris
pixels_c = []

# Initialiser la taille de l'image en charactères
total_size = 0

# Parcourir la matrice de pixels
for i in range(img.size[0]):
 for j in range(img.size[1]):
  # Recuper la valeur du pixel
  pix = str(pixel_mat[i, j][0])
  # Ajouter a la liste chaines
  pixels_c.append(pix)
  # Ajouter la longueur en charactères a la taille totale
  total_size += len(pix)
  # calcul des fréquences
  if pix in freq:
   freq[pix] += 1
  else:
   freq[pix] = 1

# Tri de la liste par ordre descendant
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])
print('   Charactere |   Huffman code ')
print('___________________________________')

for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))
    
print('')
print('')

# multiplicatiion par 8 pour avoir la taille de l'image
print('Taille sur le disque : {0} bits'.format(total_size * 8))
encoded_data = ''
for c in pixels_c:
    encoded_data = encoded_data + huffmanCode[c]
    pass
compressed_size = round(len(encoded_data))

print('')
print('')
print('Taille compressée : {0} bits '.format(compressed_size))



# operation de calcule de gain 
gain_bits = total_size * 8 - compressed_size

# Calcul du gain en pourcentages
gain_pourcent = round(gain_bits / (total_size * 8 )* 100)
print('')
print('')
print('Le gain est : ',gain_bits,' ca fait : ',gain_pourcent,'%')

