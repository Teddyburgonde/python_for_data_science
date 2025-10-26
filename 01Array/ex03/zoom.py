from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

"""
Charge l’image "animal.jpeg", effectue un zoom centré de 400×400 pixels,
extrait le canal rouge (R),
affiche le résultat et gère les erreurs éventuelles.

La fonction :
    - charge l’image via ft_load() ;
    - calcule le centre de l’image pour définir une zone de 400×400 pixels ;
    - découpe cette zone (zoom) avec la méthode crop() de Pillow ;
    - convertit la zone zoomée en tableau NumPy ;
    - extrait le canal rouge pour un affichage en niveaux de gris ;
    - affiche l’image zoomée avec les axes X et Y visibles ;
    - gère toutes les erreurs possibles
    (fichier manquant, type invalide, etc.).

Étapes principales :
    1. Charger l’image et vérifier son type.
    2. Calculer le centre et les coordonnées du zoom.
    3. Découper l’image (crop) pour obtenir la zone souhaitée.
    4. Convertir cette zone en tableau NumPy et extraire le canal rouge.
    5. Afficher la nouvelle forme et le contenu du tableau.
    6. Afficher l’image zoomée avec matplotlib.
    7. Gérer toutes les erreurs avec un try/except global.

Raises:
    FileNotFoundError: Si le fichier "animal.jpeg" est introuvable.
    TypeError: Si l’image chargée n’est pas un tableau NumPy.
    Exception: Pour toute autre erreur imprévue.

Returns:
    None
"""


def main():
    try:
        img = ft_load("animal.jpeg")
        if not isinstance(img, np.ndarray):
            raise TypeError("The loaded object is not a NumPy array.")

        # Calcul du centre et des bornes
        hauteur, largeur,  _ = img.shape
        center_x = largeur // 2
        center_y = hauteur // 2
        left = center_x - 200
        upper = center_y - 200
        right = center_x + 200
        lower = center_y + 200

        # Découpage de l'image
        img_pil = Image.open("animal.jpeg")
        zoomed_img = img_pil.crop((left, upper, right, lower))

        # Conversion et extraction du canal rouge
        array = np.array(zoomed_img)
        red_channel = array[:, :, 0]

        # Affichage l'image zoomée
        plt.imshow(red_channel, cmap='gray')
        plt.title("Zoomed Image (Red channel)")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.axis('on')
        plt.show()

        # Affiche la nouvelle forme
        print(f"New shape after slicing: (400, 400, 1) or {red_channel.shape}")
        print(red_channel)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
