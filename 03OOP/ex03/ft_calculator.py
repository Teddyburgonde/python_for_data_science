class calculator:
    """Classe permettant d'effectuer des opérations arithmétiques (addition, soustraction, multiplication, division) 
    entre un vecteur de nombres et un scalaire. 
    Les résultats sont affichés directement sans être retournés."""
    
    def __init__(self, values):
        """Initialise la calculatrice avec une liste de nombres flottants représentant le vecteur."""
        self.values = values
    
    def __add__(self, object) -> None:
        """Ajoute un scalaire à chaque élément du vecteur et affiche le résultat."""
        result = []
        for value in self.values:
            result.append(value + object)
        print(result)
        
    def __mul__(self, object) -> None:
        """Multiplie chaque élément du vecteur par un scalaire et affiche le résultat."""
        result = []
        for value in self.values:
            result.append(value * object)
        print(result)
    
    def __sub__(self, object) -> None:
        """Soustrait un scalaire à chaque élément du vecteur et affiche le résultat."""
        result = []
        for value in self.values:
            result.append(value - object)
        print(result)
    
    def __truediv__(self, object) -> None:
        """Divise chaque élément du vecteur par un scalaire et affiche le résultat.
        Si le scalaire vaut 0, affiche un message d'erreur et interrompt l'opération.
        """
        result = []
        if object == 0:
            print("You cannot divide a number by 0")
            return
        for value in self.values:
            result.append(value / object)
        print(result)