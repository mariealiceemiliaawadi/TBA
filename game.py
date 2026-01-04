# Description: Game class

# Variable de contrôle pour le debug
DEBUG = False

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from actions import talk


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
        history = Command("history", " : consulter son historique", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : afficher la liste des items présents dans cette pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre les items présents dans la pièce ", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : reposer un item dans la pièce", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : afficher l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check
        talk = Command("talk", "<personnage> : parler à un PNJ", Actions.talk, 1)
        self.commands["talk"] = talk

                
        
        # Setup rooms

        clairiere = Room("clairiere", "dans une clairière illuminée par des lucioles qui scintillent de mille feux même dans la plus grande des terreurs nocturnes.")
        self.rooms.append(clairiere)
        pont_arc = Room("pont_arc", "sur un pont magique où chaque pas que vous faites fait miraculeusement changer les couleurs autour de vous!")
        self.rooms.append(pont_arc)
        lac_miroir  = Room("lac_miroir", "près d’un lac si calme qu’il pourrait refléter votre âme… mais gare à vous car il pourrait y figer ce qu'il y a de plus profond dans votre coeur!")
        self.rooms.append(lac_miroir)
        sentier_lanternes = Room("sentier_lanternes", "sur un long sentier où des lanternes anciennes murmurent des bruits inquiétants, tellement inquiétant que même les fantômes les plus terrorisants n'osent s'y aventurer .")
        self.rooms.append(sentier_lanternes)
        pierres_cristal = Room("pierres_cristal", "devant d’énormes rochers lumineux qui illuminent le ciel si gaiement que toute la forêt y trouve sa sérénité.")
        self.rooms.append(pierres_cristal)
        jardins_fleurs = Room("jardins_fleurs", "dans un jardin magique où les fleurs dégagent un parfum si étourdissant et si enchanteur que les sirènes tentent tant bien que mal de s'en procurer.")
        self.rooms.append(jardins_fleurs)
        grotte_lumineuse = Room("grotte_lumineuse","dans une grotte scintillante dont les critaux magiques pourraient guérir n'importe quelle bête de la nature.")
        self.rooms.append(grotte_lumineuse)
        arbre_ancien = Room("arbre_ancien","au pied d’un arbre millénaire dont le tronc est couvert de symboles anciens tribaux venus des océans.")
        self.rooms.append(arbre_ancien)
        mare_brulee = Room("mare_brulee","près d’une mare bouillonnante dont l’eau noire dégage une chaleur qui pourraient vous brûler en un rien de temps.")
        self.rooms.append(mare_brulee)
        ruines_elfiques = Room("ruines_elfiques","au milieu de ruines elfiques envahies par la mousse et la magie oubliée par les elfes des Marabes, qui sont tombés amoureux des tournesols de Picana.")
        self.rooms.append(ruines_elfiques)

        # Create characters 
        Luci = Character("Luci la fée", "une petite fée lumineuse qui flotte doucement dans l’air", clairiere, ["Bienvenue voyageur… la forêt t’observe."])
        mage_pont = Character("Aeral le Mage", "un mage vêtu d’une cape changeant de couleur à chaque pas", pont_arc, ["Le pont réagit aux émotions… marche avec prudence."])
        gardien = Character("Le Gardien de Cristal", "un être ancien fait de pierre et de lumière", pierres_cristal, ["Les pierres ne parlent qu’aux âmes patientes."])
        veilleur = Character("Le Veilleur des Lanternes", "un vieil esprit silencieux tenant une lanterne tremblante", sentier_lanternes, ["Les lanternes montrent parfois ce que l’on fuit."])
        nymphe = Character("La Nymphe du lac", "une silhouette translucide émergeant de l’eau", lac_miroir, ["Prends garde… le lac ne pardonne pas."])
        dryade = Character("La Dryade des Fleurs", "une créature végétale aux yeux brillants cachée parmi les pétales", jardins_fleurs, ["Respire lentement… certaines fleurs endorment pour toujours."])

        clairiere.add_character(Luci)
        pont_arc.add_character(mage_pont)
        pierres_cristal.add_character(gardien)
        sentier_lanternes.add_character(veilleur)
        lac_miroir.add_character(nymphe)
        jardins_fleurs.add_character(dryade)

        # Create exits for rooms

        clairiere.exits = {"N": pont_arc, "O": lac_miroir, "S": sentier_lanternes, "E": None }
        pont_arc.exits = { "E": pierres_cristal, "O": lac_miroir, "S": jardins_fleurs, "N": None }
        lac_miroir.exits = {"N": pont_arc, "E": jardins_fleurs, "S": sentier_lanternes, "O": clairiere }
        sentier_lanternes.exits = {"N": clairiere, "E": jardins_fleurs, "S": lac_miroir, "O":  pont_arc }
        pierres_cristal.exits = {"N": jardins_fleurs, "E": sentier_lanternes, "S": lac_miroir, "O": pont_arc }
        jardins_fleurs.exits = {"N": pont_arc, "E": ruines_elfiques, "S": lac_miroir, "O": sentier_lanternes }
        ruines_elfiques.exits = {"O": jardins_fleurs,"N": arbre_ancien,"E": grotte_lumineuse,"S": mare_brulee}
        arbre_ancien.exits = {"S": ruines_elfiques,"O": pont_arc,"E": None,"N": None}
        grotte_lumineuse.exits = {"O": ruines_elfiques,"S": pierres_cristal,"N": None,"E": None}
        mare_brulee.exits = {"N": ruines_elfiques,"O": sentier_lanternes,"E": None,"S": None}

        for room in self.rooms :
            self.directions.update(room.exits.keys())
        
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = pont_arc

        # Create enchanted forest items
        baton_lumineux = Item("baton","un bâton ancien gravé de runes, diffusant une douce lumière",2)
        poussiere_fee = Item("poussiere","une poudre scintillante laissée par les fées de la forêt",1)
        feuille_ancestrale = Item("feuille","une feuille dorée chargée de magie protectrice",1)
        pierre_chantante = Item("pierre","une pierre mystérieuse qui murmure lorsque vous l'approchez",2)
        lanterne_elfique = Item("lanterne","une lanterne elfique éclairant même les ténèbres magiques",2)
        fleur_somnolente = Item("fleur","une fleur enchantée dont le parfum peut endormir les imprudents",1)
        racine_magique = Item("racine", "une racine noueuse imprégnée de magie ancienne", 2)
        pierre_chaude = Item("charbon", "une pierre brûlante issue du coeur séché d'un arbre ", 2)
        tablette_elfique = Item("tablette", "une tablette gravée de runes elfiques", 3)
        cristal_pur = Item("cristal_pur", "un cristal d'une pureté exceptionnelle, concu pour apaiser les chagrins amoureux", 2)

        # Place enchanted items in rooms

        clairiere.inventory["baton"] = baton_lumineux
        pont_arc.inventory["lanterne"] = lanterne_elfique
        lac_miroir.inventory["pierre"] = pierre_chantante
        sentier_lanternes.inventory["poussiere"] = poussiere_fee
        pierres_cristal.inventory["feuille"] = feuille_ancestrale
        jardins_fleurs.inventory["fleur"] = fleur_somnolente
        arbre_ancien.inventory["racine"] = racine_magique
        mare_brulee.inventory["charbon"] = pierre_chaude
        ruines_elfiques.inventory["tablette"] = tablette_elfique
        grotte_lumineuse.inventory["cristal_pur"] = cristal_pur

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))

            # Déplacer tous les PNJ après chaque commande
            for room in self.rooms:
                for character in room.characters[:]:  # copie de la liste
                    moved = character.move()
                    if moved and DEBUG:
                        print(f"DEBUG: {character.name} s'est déplacé")

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split()

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
        print(f"\nBienvenue {self.player.name} dans cet univers magique !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
