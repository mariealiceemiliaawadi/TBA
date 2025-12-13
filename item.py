#Cette classe sera utilisée pour représenter les différents objets que le joueur pourra trouver dans les différents lieux de la map.
# Description: Classe représentant un objet dans le jeu.

class Item:
    """
    Représente un objet que le joueur peut trouver dans le jeu.
    """
    
    # Constructeur
    def __init__(self, name: str, description: str, weight: int):
        """
        Initialise un nouvel objet.

        :param name: Le nom de l'objet (ex: "sword").
        :param description: Une brève description (ex: "une épée au fil tranchant").
        :param weight: Le poids de l'objet, en kg.
        """
        self.name = name #le nom de l’objet
        self.description = description #la description de l’objet
        self.weight = weight #le poids de l’objet

    # Redéfinition de la méthode __str__
    def __str__(self):
        """
        Retourne une représentation textuelle conviviale de l'objet, 
        incluant son nom, sa description et son poids.
        
        Format attendu : "nom : description (poids kg)"
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"

