# * *args contient une liste de nombres (ex: 1, 42, 360...). 
# * **kwargs contient les mots-clés qui indiquent les calculs à faire (ex: mean, median, var...). 

def ft_statistics(*args: Any, **kwargs: Any) -> None:
	"""Calcule et affiche différentes statistiques (moyenne, médiane, quartiles, écart-type, variance)
    selon les options demandées dans les paramètres nommés (**kwargs).
    
    - *args : contient les nombres sur lesquels faire les calculs.
    - **kwargs : indique quelles statistiques afficher (ex: mean, median, var...).
    - Si aucun nombre n’est fourni ou qu’une option est inconnue, affiche 'ERROR'.
    """
	if (len(args) == 0) or not kwargs:
		print("ERROR")
		return
	valid_options = ["mean", "median", "quartile", "std", "var"]
	for k, value in kwargs.items():
		if value not in valid_options:
			print("ERROR")
			return

# Étape 4 : Calculer les statistiques ❌

# * mean : moyenne → somme(args) / len(args). ❌
# * median : valeur du milieu après tri. ❌

#   * Si la longueur est impaire → valeur centrale. ❌
#   * Si elle est paire → moyenne des deux valeurs centrales. ❌
# * quartile : valeurs aux positions 25% et 75%. ❌

#   * Exemple : pour [11, 42, 64, 360], quartiles = [11.0, 64.0]. ❌
# * std : écart-type → racine carrée de la variance. ❌
# * var : variance → moyenne des carrés des écarts à la moyenne. ❌

# Étape 5 : Lire les options demandées ❌

# * Parcourir chaque élément de **kwargs. ❌
# * Pour chaque valeur (ex: "mean"), faire le calcul correspondant. ❌
# * Si la clé ne correspond à aucun calcul connu → afficher "ERROR". ❌

# Étape 6 : Afficher les résultats ❌

# * Pour chaque calcul réussi, afficher : nom du calcul + ":" + résultat. ❌
# * Exemple :

#   * mean : 95.6 ❌
#   * median : 42 ❌
#   * quartile : [11.0, 64.0] ❌

# Étape 7 : Vérification finale ❌

# * Tous les calculs affichent le bon résultat. ❌
# * Les erreurs sont bien gérées (3 erreurs affichées dans le dernier test). ❌
# * Le code respecte la norme flake8 et ne contient pas d’import interdit. ❌
