# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = {}
        self.history = []

    def get_history(self):
        if not self.history:
            return "Aucune pièce visitée pour le moment."

        s = "Vous avez déjà visité les pièces suivantes :\n"
        for room in self.history:
            s += f"- {room.name}\n"
        return s


    # Return a string describing the player's inventory.
    def get_inventory(self):
        # If the inventory is empty.
        if not self.inventory:
            return "Votre inventaire est vide."

        inventory_string = "Vous disposez des items suivants :\n"
        for item in self.inventory.values():
            inventory_string += f"- {item}\n"
        return inventory_string

    
    def move(self, direction):
        
        next_room = self.current_room.exits[direction]

       
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        
        self.history.append(self.current_room)

        
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    