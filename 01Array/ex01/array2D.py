def slice_me(family: list, start: int, end: int) -> list:
    """
    Découpe une liste 2D (matrice) entre les lignes `start` et `end`,
    affiche la forme avant et après découpage,
    puis renvoie la portion découpée.

    Args:
        family (list): Une liste 2D (liste de listes) représentant la matrice.
        start (int): L’indice de début pour le découpage.
        end (int): L’indice de fin pour le découpage (non inclus).

    Returns:
        list: Une nouvelle liste 2D contenant les lignes découpées.

    Raises:
        TypeError: Si `family` n’est pas une liste de listes,
                   ou si `start`/`end` ne sont pas des entiers.
        ValueError: Si les sous-listes n’ont pas toutes la même longueur.
    """
    if type(family) is not list:
        raise ValueError("family must be a list")
    for f in family:
        if not isinstance(f, (list)):
            raise TypeError("All family values must be list.")
    first_len = len(family[0])
    for f in family:
        if len(f) != first_len:
            raise ValueError("All sublists must have the same length.")
    if type(start) is not int or type(end) is not int:
        raise ValueError("start and end must be integers")
    print(f"My shape is: ({len(family)}, {len(family[0])})")
    sliced = family[start:end]
    print(f"My new shape is : ({len(sliced)}, {len(sliced[0])})")
    return sliced
