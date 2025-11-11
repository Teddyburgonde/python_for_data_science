from abc import ABC


class Character(ABC):
    """
    Classe abstraite représentant un personnage du monde de Game of Thrones.

    Attributs :
    -----------
    first_name : str
    Le prénom du personnage.
    is_alive : bool
    Indique si le personnage est encore en vie (True par défaut).

    Méthodes :
    ----------
    die():
    Change l’état du personnage en le marquant comme mort.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialise un nouveau personnage.

        Paramètres :
        -------------
        first_name : str
        Le prénom du personnage.
        is_alive : bool, optionnel
        Indique si le personnage est vivant (True par défaut).
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Marque le personnage comme mort en définissant is_alive à False."""
        self.is_alive = False


class Stark(Character):
    """
    Classe représentant un membre de la famille Stark, héritant de Character.

    Attributs :
    -----------
    first_name : str
    Le prénom du membre de la famille Stark.
    is_alive : bool
    Indique si le personnage est encore en vie (True par défaut).

    Remarques :
    -----------
    Les Stark sont connus pour leur loyauté et leur honneur.
    """
    def __init__(self, first_name, is_alive=True):
        """Initialise un membre de la famille Stark."""
        super().__init__(first_name, is_alive)
