from quest import QuestManager
class Player():
    """docstring"""
    # Define the constructor
    def __init__(self, name,max_weight=15): 
        self.name = name 
        self.current_room = None 
        self.history = []
        self.inventory = [] 
        self.max_weight = max_weight
        self.quests = QuestManager(self)
        self.errors = 0 # On commence à 0 erreur
        
    # Define the move method. 
    def move(self, direction): 
        # Get the next room from the exits dictionary of the current room. 
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.history.append(self.current_room)

        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        if not self.history: 
            return "Aucune pièce visitée pour le moment." 
        s = "Vous avez déjà visité les pièces suivantes:\n" 
        for room in self.history: 
            s += f"     - {room.description}\n" 
        return s

    def back(self): 
        if not self.history: 
            print("Impossible de revenir en arrière, aucun déplacement effectué.")
            return False
        self.current_room = self.history.pop()

        print(self.current_room.get_long_description()) 
        print(self.get_history()) 
        return True

    def get_inventory(self):
        if not self.inventory:
            return "Votre inventaire est vide."
        s = "Vous disposez des items suivants :\n"
        for item in self.inventory:
            s += f"    - {item}\n"
        return s

    def check_inventory_weight(self):
        return sum(item.weight for item in self.inventory)

    def take(self, item_name):
        room_items = self.current_room.inventory
        item = next((i for i in room_items if i.name.lower() == item_name.lower()), None)
        if not item:
            print(f"L'objet '{item_name}' n'est pas dans la pièce.")
            return False
        if self.check_inventory_weight() + item.weight > self.max_weight:
            print(f"Vous ne pouvez pas prendre '{item_name}', trop lourd.")
            return False
        self.inventory.append(item)
        room_items.remove(item)
        print(f"Vous avez pris l'objet '{item_name}'.")
        return True

    def drop(self, item_name):
        room_items = self.current_room.inventory
        item = next((i for i in self.inventory if i.name.lower() == item_name.lower()), None)
        
        if not item:
            print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")
            return False
        
        self.inventory.remove(item)
        room_items.append(item)
        
        print(f"Vous avez déposé l'objet '{item.name}'.")
        return True