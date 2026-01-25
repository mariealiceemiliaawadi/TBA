# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = []
        self.characters = {}
    
    # Define the get_exit method.
    def get_exit_string(self):
        exit_string = "Sorties:"
        for direction, neighbor in self.exits.items():
            if neighbor is not None:
                exit_string += f"\n\t- {direction} : {neighbor.name}"
        return exit_string
            
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: "
        for direction, neighbor in self.exits.items():
            if neighbor is not None:
                exit_string += f"\n\t- {direction} -> {neighbor.description}"
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        desc = f"\nVous êtes {self.description}\n"
        desc += self.get_characters_description()
        desc += f"\n\n{self.get_exit_string()}"
        return desc

    def get_inventory(self):
        if not self.inventory:
            return "Il n'y a rien ici."
        s = "La pièce contient :\n"
        for item in self.inventory:
            s += f"    - {item}\n"
        return s

    def look(self):
        print(self.get_inventory())

    def add_character(self, character):
        self.characters[character.name] = character


    def get_characters_description(self):
        if not self.characters:
            return ""
        lines = "\nPersonnages présents :"
        for name in self.characters:
            lines += f"\n- {name}"
        return lines
