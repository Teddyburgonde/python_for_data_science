"""
ROADMAP – Fonction zoom()
🎯 Objectif :
Charger l’image animal.jpeg, effectuer un zoom centré de 400×400 pixels, 
extraire un seul canal (par exemple le rouge),
puis afficher le résultat avec les axes X et Y visibles.
Étapes:
4. Récupérer la taille de l’image
Obtenir la largeur et la hauteur de l’image pour pouvoir calculer son centre.
5. Calculer la zone du zoom
Déterminer les coordonnées d’un carré 400×400 pixels centré :
trouver le centre (center_x, center_y)
définir les bornes (left, upper, right, lower)
6. Découper l’image (crop)
Créer une nouvelle image contenant seulement cette zone (le zoom).
7. Convertir la zone zoomée en tableau NumPy
Transformer cette zone en tableau pour pouvoir manipuler les canaux de couleur.
8.Extraire un seul canal de couleur
Par exemple, garder seulement le canal rouge (R) de l’image zoomée.
9. Afficher les informations du nouveau tableau
Afficher :
la nouvelle forme du tableau (400×400 ou 400×400×1)
et le contenu des pixels de ce canal.
10. Afficher l’image zoomée
Utiliser matplotlib pour afficher le canal extrait :
en niveaux de gris (cmap='gray')
avec les axes visibles (xlabel, ylabel, title, axis('on'))
11. Gérer les erreurs
Entourer le tout d’un try/except pour capturer les erreurs :
fichier manquant,
problème de découpage,
ou autre erreur imprévue.
"""

from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = ft_load("animal.jpeg")
if not isinstance(img, np.ndarray):
    raise TypeError("The loaded object is not a NumPy array.")

