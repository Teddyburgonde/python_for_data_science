import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Génère un identifiant aléatoire composé de 15 lettres minuscules.
    Cet identifiant est utilisé automatiquement pour chaque nouvel étudiant.
    """
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    """
    Représente un étudiant avec un nom, un prénom, un login généré automatiquement
    et un identifiant unique généré via generate_id().
    
    - name : prénom de l'étudiant
    - surname : nom de famille de l'étudiant
    - active : indique si l'étudiant est actif (toujours True par défaut)
    - login : généré automatiquement à partir du prénom et du nom
    - id : identifiant unique généré automatiquement
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)
    
    def __post_init__(self):
        """
        Génère automatiquement le login de l'étudiant : première lettre du prénom en majuscule
        suivie du nom de famille (ex : Edward + agle → Eagle).
        """
        self.login = self.name[0].upper() + self.surname