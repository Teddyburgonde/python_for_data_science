"""
Ce programme illustre l'utilisation d'une fonction imbriquée (closure) en Python.

La fonction outer(x, y, z) définit et retourne une fonction interne inner(a),
qui calcule et affiche le résultat de x**a + y**a + z**a.
"""

def square(x: int | float) -> int | float:
	"""Renvoie le carré du nombre x. 
	Exemple : square(3) → 9"""
	nb_square = x ** 2
	return nb_square

def pow(x: int | float) -> int | float:
	"""pow(x) doit retourner x exposant x
	Exemple : pow(2) = 2² = 4
	"""
	nb_pow = x ** x
	return nb_pow

def outer(x: int | float, function) -> object:
	"""Fonction externe (closure) qui reçoit un nombre x et une fonction (comme square ou pow).
	Elle crée une fonction interne inner() qui applique la fonction à x à chaque appel
	et garde en mémoire le nombre d'appels effectués.
	"""
	count = 0
	def inner() -> float:
		nonlocal count  # pour pouvoir modifier count à l’intérieur
		nonlocal x
		count += 1
		x = function(x)
		return x
