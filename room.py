# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = []
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a string describing the room's inventory.
    def get_inventory(self):
        result = ""
        # Affichage des items
        for item in self.inventory.values():
            result += f"- {item.name} : {item.description} ({item.weight} kg)\n"
        
        # Affichage des personnages non joueurs
        for character in self.characters:
            result += f"- {character.name} : {character.description}\n"
        
        if result == "":
            return "Il n'y a rien ici."
        return result

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def add_character(self, character):
        self.characters.append(character)
