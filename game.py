# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.directions = set()
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        look = Command("look", " : afficher la liste des items présents dans cette pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre les items présents dans la pièce ", Actions.take, 1)
        self.commands["take"] = take
        
        # Setup rooms

        clairiere = Room("clairiere", "dans une clairière illuminée par des lucioles qui ne disparaissent jamais.")
        self.rooms.append(clairiere)
        pont_arc = Room("pont_arc", "sur un pont magique où chaque pas fait changer les couleurs autour de vous.")
        self.rooms.append(pont_arc)
        lac_miroir  = Room("lac_miroir", "près d’un lac si calme qu’il reflète votre âme… mais il peut vous figer pour toujours.")
        self.rooms.append(lac_miroir)
        sentier_lanternes = Room("sentier_lanternes", "sur un long sentier où des lanternes anciennes murmurent des bruits inquiétants.")
        self.rooms.append(sentier_lanternes)
        pierres_cristal = Room("pierres_cristal", "devant d’énormes rochers lumineux qui battent comme un cœur vivant.")
        self.rooms.append(pierres_cristal)
        jardins_fleurs = Room("jardins_fleurs", "dans un jardin magique où les fleurs dégagent un parfum étourdissant et dangereux.")
        self.rooms.append(jardins_fleurs)

        # Create exits for rooms

        clairiere.exits = {"N": pont_arc, "O": lac_miroir, "S": sentier_lanternes, "E": None }
        pont_arc.exits = { "E": pierres_cristal, "O": lac_miroir, "S": jardins_fleurs, "N": None }
        lac_miroir.exits = {"N": pont_arc, "E": jardins_fleurs, "S": sentier_lanternes, "O": clairiere }
        sentier_lanternes.exits = {"N": clairiere, "E": jardins_fleurs, "S": lac_miroir, "O":  pont_arc }
        pierres_cristal.exits = {"N": jardins_fleurs, "E": sentier_lanternes, "S": lac_miroir, "O": pont_arc }
        jardins_fleurs.exits = {"N": pont_arc, "E": None, "S": lac_miroir, "O": sentier_lanternes }

        for room in self.rooms :
            self.directions.update(room.exits.keys())
        
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = pont_arc

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
