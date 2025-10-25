from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Charge une image à partir d'un chemin de fichier,
    la convertit en tableau NumPy
    au format RGB, affiche sa forme (hauteur, largeur, canaux),
    puis retourne ce tableau.

    Args:
        path (str): Le chemin vers le fichier image à charger.

    Returns:
        numpy.ndarray: L'image représentée sous forme
        de tableau NumPy (en RGB).

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
        OSError: Si le fichier ne peut pas être ouvert
        ou n'est pas une image valide.
    """
    img = Image.open(path)
    array = np.array(img)
    print(f"The shape of image is: {array.shape}")
    return array
