def give_bmi(
    height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calcule l'indice de masse corporelle (IMC) pour chaque paire taille/poids.

    La fonction parcourt les deux listes données (tailles et poids) et calcule
    pour chaque paire l'IMC à l'aide de la formule suivante :
        IMC = poids / (taille ** 2)

    :param height:
        Liste des tailles (en mètres).
    :param weight:
        Liste des poids (en kilogrammes).
    :returns:
        Une liste contenant toutes les valeurs d'IMC calculées (float).

    :example:
        >>> give_bmi([1.80, 1.60], [75, 60])
        [23.148148148148145, 23.437499999999996]
    """
    if (type(height) is not list or type(weight) is not list):
        raise ValueError("height and weight must be a list")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("All height values must be int or float.")
    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("All weight values must be int or float.")
    bmi_list = []
    for h, w in zip(height, weight):
        bmi = w / (h ** 2)
        bmi_list.append(bmi)
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare chaque valeur d'IMC à une limite
    donnée et retourne une liste de booléens.

    La fonction parcourt la liste d'IMC et indique, pour chaque valeur,
    si elle dépasse ou non la limite spécifiée.

    :param bmi:
        Liste des valeurs d'IMC (float ou int).
    :param limit:
        Limite de comparaison (entier).
    :returns:
        Une liste de booléens :
            True si l'IMC est supérieur à la limite, False sinon.

    :example:
        >>> apply_limit([22.5, 29.0], 26)
        [False, True]
    """
    if type(bmi) is not list:
        raise TypeError("bmi must be a list")
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise ValueError("All height values must be int or float.")
    if not isinstance(limit, int):
        raise ValueError("limit must be int")
    apply_list = []
    for b in bmi:
        if b > limit:
            apply_list.append(True)
        else:
            apply_list.append(False)
    return apply_list
