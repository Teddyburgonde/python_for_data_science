"""
Objectif :
Créer une fonction ft_load() qui ouvre une image, 
affiche ses informations et retourne ses pixels sous forme de tableau.

Étapes :
1. Importer une bibliothèque pour ouvrir l’image (ex : PIL) et une pour la convertir en tableau (ex : NumPy).
2. Ouvrir le fichier image à partir du chemin reçu en paramètre.
3. Vérifier que le format de l’image est bien JPG ou JPEG.
4. Convertir l’image en tableau (valeurs RGB).
5. Afficher la forme du tableau (hauteur, largeur, canaux).
6. Afficher le contenu des pixels (le tableau complet).
7. Retourner ce tableau.
8. Gérer les erreurs : fichier manquant, format invalide, problème de lecture.
"""

from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Charge une image depuis un chemin de fichier, affiche ses informations,
    et retourne son contenu sous forme de tableau NumPy en valeurs RGB.

    La fonction :
        - ouvre l’image spécifiée ;
        - vérifie que le format est bien JPEG ou JPG ;
        - convertit l’image en tableau NumPy ;
        - affiche la forme du tableau (hauteur, largeur, canaux) ;
        - affiche le contenu des pixels ;
        - gère les erreurs courantes (fichier introuvable, format invalide, etc.).

    Args:
        path (str): Le chemin vers le fichier image à charger.

    Returns:
        numpy.ndarray: L’image convertie en tableau NumPy au format RGB.

    Raises:
        FileNotFoundError: Si le fichier n’existe pas.
        ValueError: Si le format de l’image n’est pas JPEG ou JPG.
        Exception: Pour toute autre erreur imprévue lors du chargement.
    """
    try:
        img = Image.open(path)
        if img.format not in ["JPEG", "JPG"]:
            raise ValueError("Only JPEG and JPG formats are supported.")
        array = np.array(img)
        print(array.shape)
        print(array)
        return array

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")