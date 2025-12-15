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

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        #Ajouter la room actuelle dans l'historique
        self.history.append(self.current_room)

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    