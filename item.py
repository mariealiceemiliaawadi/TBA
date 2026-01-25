# item.py

class Item:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight
        self.original_room = None

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"


class RoomWithItems:
    """Classe à utiliser pour les pièces contenant des items"""
    def __init__(self):
        self.inventory = []

    def get_inventory(self):
        if not self.inventory:
            return "Il n'y a rien ici."
        s = "La pièce contient :\n"
        for item in self.inventory:
            s += f"    - {item}\n"
        return s

    def look(self):
        print(self.get_inventory())


class PlayerWithItems:
    """Classe à utiliser pour le joueur"""
    def __init__(self, max_weight=10):
        self.inventory = []
        self.max_weight = max_weight

    def get_inventory(self):
        if not self.inventory:
            return "Votre inventaire est vide."
        s = "Vous disposez des items suivants :\n"
        for item in self.inventory:
            s += f"    - {item}\n"
        return s

    def check(self):
        print(self.get_inventory())

    def take(self, item_name, current_room):
        for item in current_room.inventory:
            if item.name.lower() == item_name.lower():
                total_weight = sum(i.weight for i in self.inventory)
                if total_weight + item.weight > self.max_weight:
                    print(f"Vous ne pouvez pas prendre '{item.name}', trop lourd !")
                    return False
                self.inventory.append(item)
                current_room.inventory.remove(item)
                print(f"Vous avez pris l'objet '{item.name}'.")
                return True
        print(f"L'objet '{item_name}' n'est pas dans la pièce.")
        return False

    def drop(self, item_name, current_room):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                current_room.inventory.append(item)
                print(f"Vous avez déposé l'objet '{item.name}'.")
                return True
        print(f"L'objet '{item_name}' n'est pas dans l'inventaire.")
        return False
 