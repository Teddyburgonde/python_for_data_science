class calculator:
	"""Classe permettant d'effectuer des calculs entre deux vecteurs de même taille.
    Les résultats sont affichés directement sans être retournés.
    """

	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		"""Calcule et affiche le produit scalaire (dot product) de deux vecteurs."""
		if len(V1) != len(V2):
			print("Error: vectors must be the same size.")
			return
		result = []
		for x, y in zip(V1, V2):
			result.append(x  * y)
		print("Dot product is:", sum(result))

	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		"""Calcule et affiche la somme de deux vecteurs (élément par élément)."""
		if len(V1) != len(V2):
			print("Error: vectors must be the same size.")
			return
		result = []
		for x, y in zip(V1, V2):
			result.append(float(x) + float(y))
		print("Add Vector is :", result)

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		"""Calcule et affiche la différence entre deux vecteurs (élément par élément)."""
		if len(V1) != len(V2):
			print("Error: vectors must be the same size.")
			return
		result = []
		for x, y in zip(V1, V2):
			result.append(float(x) - float(y))
		print("Sous Vector is:", result)
