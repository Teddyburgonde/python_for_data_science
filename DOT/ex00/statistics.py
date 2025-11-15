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

        if value == "mean":
            """Calcule et affiche la moyenne des valeurs."""
            mean = sum(args) / len(args)
            print("mean :", mean)

		if value == "median":
		    """Calcule et affiche la médiane des valeurs."""
            sorted_args = sorted(args)
            if (len(sorted_args) % 2 == 0):
                mid = len(sorted_args)//2
                median = (sorted_args[mid - 1] + sorted_args[mid]) / 2
            else:
                median = sorted_args[len(sorted_args)//2]
            print("median :", median)

        if value == "quartile":
            """Calcule et affiche les quartiles (25% et 75%) des valeurs."""
            sorted_args = sorted(args)
            n = len(sorted_args)
            q1_index = int(0.25 * (n - 1))
            q3_index = int(0.75 * (n - 1))
            q1 = float(sorted_args[q1_index])
            q3 = float(sorted_args[q3_index])
            print("quartile :", [q1, q3])

        if value == "std":
            """Calcule et affiche l'écart-type des valeurs."""
            mean = sum(args) / len(args)
            squared_diffs = [(x - mean) ** 2 for x in args]  # différences au carré
            variance = sum(squared_diffs) / len(args) # moyenne des carrés
            std = variance ** 0.5 # racine carrée de la variance
            print("std :", std)

        if value == "var":
            """Calcule et affiche la variance des valeurs."""
            mean = sum(args) / len(args)
            squared_diffs = [(x - mean) ** 2 for x in args]  # différences au carré
            variance = sum(squared_diffs) / len(args) # moyenne des carrés   
            print("variance :", variance)
