from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

"""
Charge l’image "animal.jpeg", découpe un carré centré de 400×400 pixels,
effectue une transposition manuelle (échange lignes ↔ colonnes),
puis affiche le résultat en niveaux de gris.

La fonction :
    - charge l’image via ft_load() depuis load_image.py ;
    - vérifie que l’image chargée est bien un tableau NumPy ;
    - calcule le centre de l’image pour définir une zone de 400×400 pixels ;
    - découpe cette zone avec la méthode crop() de Pillow ;
    - convertit cette zone en tableau NumPy ;
    - extrait le canal rouge pour obtenir une image en niveaux de gris ;
    - transpose la matrice manuellement,
    sans utiliser de bibliothèque externe ;
    - affiche la nouvelle forme et les données après transposition ;
    - affiche le résultat final avec matplotlib, avec les axes visibles ;
    - gère toutes les erreurs possibles
    (fichier manquant, mauvais format, etc.).

Étapes principales :
    1. Charger l’image et vérifier son type.
    2. Calculer le centre et définir la zone 400×400.
    3. Découper l’image avec Pillow.
    4. Convertir en tableau NumPy et extraire le canal rouge.
    5. Appliquer une transposition manuelle.
    6. Afficher la nouvelle forme et les données.
    7. Afficher l’image transposée avec matplotlib.
    8. Gérer toutes les erreurs avec un bloc try/except.

Raises:
    FileNotFoundError: Si le fichier "animal.jpeg" est introuvable.
    TypeError: Si l’image chargée n’est pas un tableau NumPy.
    Exception: Pour toute autre erreur imprévue
    (ex: problème de découpe ou de type).
"""


def transpose_image(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose manuellement une matrice (échange lignes et colonnes)."""
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        transposed.append(new_row)
    return transposed


def main():
    try:
        img = ft_load("animal.jpeg")
        if not isinstance(img, np.ndarray):
            raise TypeError("The loaded object is not a NumPy array.")

        # Calcul du centre et découpe
        hauteur, largeur, _ = img.shape
        center_x = largeur // 2
        center_y = hauteur // 2
        left = center_x - 200
        upper = center_y - 200
        right = center_x + 200
        lower = center_y + 200

        # Découpage de l'image
        img_pil = Image.open("animal.jpeg")
        cropped_img = img_pil.crop((left, upper, right, lower))

        # Conversion et extraction du canal rouge
        array = np.array(cropped_img)
        red_channel = array[:, :, 0]

        # Transposition manuelle
        transposed_arr = np.array(transpose_image(red_channel.tolist()))

        # Affichage des infos
        print(f"New shape after Transpose: {transposed_arr.shape}")
        print(transposed_arr)

        # Affichage de l'image transposée
        plt.imshow(transposed_arr, cmap='gray')
        plt.title("Transposed Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.axis('on')
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
