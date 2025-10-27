import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Charge un fichier CSV et le renvoie sous forme de DataFrame pandas.

    La fonction tente de lire le fichier CSV situé à l’emplacement indiqué
    par le paramètre `path`. Si le fichier est chargé avec succès, elle
    affiche ses dimensions (lignes, colonnes) et retourne le DataFrame.
    En cas d’erreur (fichier introuvable, format invalide, etc.), elle
    affiche un message d’erreur et retourne None.

    :param path:
        Le chemin d’accès vers le fichier CSV à charger.
    :returns:
        Un DataFrame pandas contenant les données du fichier, ou None
        en cas d’erreur de lecture.

    :example:
        >>> load("life_expectancy_years.csv")
        Loading dataset of dimensions (195, 302)
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except Exception as e:
        print(f"Error: {e}")
        return None
