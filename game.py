from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from quest import Quest
from quest import QuestManager
from character import Character

class Game:

    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.directions = {"N": ["N", "NORD"],"S": ["S", "SUD"],"E": ["E", "EST"],"O": ["O", "OUEST"]}
    
    def setup(self):
        name = input("Entrez votre nom: ")
        self.player = Player(name)

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        history_cmd = Command("history", " : afficher l'historique des pièces visitées", lambda game, lw, np: print(game.player.get_history()) or True, 0)
        self.commands["history"] = history_cmd
        back_cmd = Command("back", " : revenir à la pièce précédente", lambda game, lw, np: game.player.back(), 0)
        self.commands["back"] = back_cmd
        look_cmd = Command("look", " : observer la pièce", Actions.look, 0)
        self.commands["look"] = look_cmd
        take_cmd = Command("take", " <item> : prendre un objet", Actions.take, 1)
        self.commands["take"] = take_cmd
        drop_cmd = Command("drop", " <item> : déposer un objet", Actions.drop, 1)
        self.commands["drop"] = drop_cmd
        check_cmd = Command("check", " : vérifier votre inventaire", Actions.check, 0)
        self.commands["check"] = check_cmd
        quests_cmd = Command("quests", ": permet de voir la liste des quêtes et leur progression.", Actions.quests, 0)
        self.commands["quests"]= quests_cmd

        clairiere = Room("clairiere", "dans une clairière illuminée par des lucioles.")
        self.rooms.append(clairiere)
        pont_arc = Room("pont arc", "sur un pont magique aux couleurs mouvantes.")
        self.rooms.append(pont_arc)
        lac_miroir = Room("lac miroir", "près d’un lac reflétant l’âme.")
        self.rooms.append(lac_miroir)
        sentier_lanternes = Room(" sentier lanternes", "sur un sentier hanté de lanternes.")
        self.rooms.append( sentier_lanternes)
        pierres_cristal= Room("pierres cristal", "devant des rochers lumineux.")
        self.rooms.append(pierres_cristal)
        jardins_fleurs = Room("jardins fleurs", "dans un jardin enivrant.")
        self.rooms.append(jardins_fleurs)
        grotte_lumineuse  = Room("grotte lumineuse ", "dans une grotte scintillante.")
        self.rooms.append(grotte_lumineuse )
        arbre_ancien = Room("arbre ancien", "au pied d’un arbre ancien.")
        self.rooms.append(arbre_ancien)
         
        potion_magique = Item("la potion magique", "la potion qui ensorcelait les géants", 2)
        baguette_magique = Item("la baguette magique", "une baguette qui sait ce qu'elle fait!", 1)
        la_guirlande_suédoise = Item("la fameuse guirlande suédoise", "La Suède n'a qu'à bien se tenir!", 1)
        la_fleur_amoureuse= Item("la fleur amoureuse de l'amour","la fleur qui aimait aimer. ",1)
        le_miroir_fluorescent= Item("le miroir fluorescent","le miroir qui était coloré de mille étoiles",1)
        la_branche_enchantée= Item("la branche enchantée","la branche qui volait de ses propres ailes.",1)
        le_peigne_poussant= Item("le peigne poussant","Ce peigne avait la possibilité de faire pousser les cheveux en un rien de temps!",1)
        
        
        
        la_guirlande_suédoise.original_room = clairiere
        potion_magique.original_room = sentier_lanternes
        la_fleur_amoureuse.original_room = jardins_fleurs
        le_peigne_poussant.original_room = pierres_cristal
        baguette_magique.original_room =  grotte_lumineuse
        la_branche_enchantée.original_room =  pont_arc
        le_miroir_fluorescent.original_room = lac_miroir




        sentier_lanternes.inventory.append(potion_magique)
        jardins_fleurs.inventory.append(la_fleur_amoureuse)
        pierres_cristal.inventory.append( le_peigne_poussant)  
        lac_miroir.inventory.append(le_miroir_fluorescent)
        clairiere.inventory.append(la_guirlande_suédoise)
        grotte_lumineuse.inventory.append(baguette_magique)
        pont_arc.inventory.append(la_branche_enchantée)
          
        clairiere.exits = {"N": pont_arc}
        pont_arc.exits = {"S": clairiere, "E": jardins_fleurs}
        jardins_fleurs.exits = {"O": pont_arc, "N": sentier_lanternes}
        sentier_lanternes.exits = {"S": jardins_fleurs, "O": lac_miroir}
        lac_miroir.exits = {"E": sentier_lanternes, "S": pierres_cristal}
        pierres_cristal.exits = {"N": lac_miroir, "O": grotte_lumineuse}
        grotte_lumineuse.exits = {"E": pierres_cristal, "N": arbre_ancien}
        arbre_ancien.exits = {"S": grotte_lumineuse}

        self.player.current_room = clairiere

        self.q_final = Quest("L'éveil de l'Arbre", "Atteindre l'Arbre Ancien pour terminer l'aventure", ["Visiter arbre_ancien"])
        self.q_items = Quest(
    "Collectionneur", 
    "Récupérer les 7 objets magiques présents dans chaque salle!!!!", 
    [
        "Prendre la potion magique", 
        "Prendre la fleur amoureuse de l'amour", 
        "Prendre le peigne poussant", 
        "Prendre le miroir fluorescent", 
        "Prendre la fameuse guirlande suédoise", 
        "Prendre la baguette magique", 
        "Prendre la branche enchantée"
    ]
)
        
        self.player.quests.add_quest(self.q_final)
        self.player.quests.add_quest(self.q_items)

        questions_reponses = {
            "Combien font ((3*6)+4)/11 ?": "2",
            "Combien de pattes a une araignée ?": "8",
            "Quel insecte fabrique du miel ?": "abeille",
            "Combien font 7 x 8 ?": "56",
            "De quelle couleur est la chlorophylle ?": "verte",
            "Combien de couleurs dans un arc-en-ciel ?": "7",
            "Quel est le résultat de 100 divisé par 4 ?": "25",
            "Quel animal se transforme en papillon ?": "chenille",
            "Combien font 10 + 10 x 0 ?": "10",
            "Quel arbre produit des glands ?": "chene",
            "Si j'ai 3 pommes et que j'en mange une, combien en reste-t-il ?": "2",
            "Combien font 12 au carré ?": "144",
            "Combien de côtés a un hexagone ?": "6",
            "Quel est le chiffre romain pour 10 ?": "x",
            "Combien font 9 x 9 ?": "81",
            "Quel nombre vient après 999 ?": "1000",
            "Combien de secondes dans une minute ?": "60",
            "La moitié de 50 ?": "25",
            "Combien de degrés dans un angle droit ?": "90",
            "Combien de faces a un cube ?": "6",
            "Quelle est la capitale de l'Autriche ?": "vienne",
            "Quelle est la capitale de la France ?": "paris",
            "Quelle est la capitale de l'Italie ?": "rome",
            "Quelle est la capitale de l'Espagne ?": "madrid",
            "Quelle est la capitale de l'Allemagne ?": "berlin",
            "Quelle est la capitale du Royaume-Uni ?": "londres",
            "Quelle est la capitale du Japon ?": "tokyo",
            "Quelle est la capitale de la Chine ?": "pekin",
            "Quelle est la capitale des États-Unis ?": "washington",
            "Quelle est la capitale de la Russie ?": "moscou",
            "Comment dit-on 'chat' en anglais ?": "cat",
            "Comment dit-on le foie en anglais ?": "liver",
            "Comment dit-on 'chien' en anglais ?": "dog",
            "Comment dit-on 'maison' en anglais ?": "house",
            "Traduire 'Red' en français ?": "rouge",
            "Comment dit-on 'pomme' en anglais ?": "apple",
            "Comment dit-on 'livre' en anglais ?": "book",
            "Traduire 'Sun' en français ?": "soleil",
            "Comment dit-on 'école' en anglais ?": "school",
            "Comment dit-on 'eau' en anglais ?": "water",
            "Quel est le pays le plus peuplé du monde ?": "inde",
            "Quel est le plus grand océan ?": "pacifique",
            "Dans quel pays se trouve la Tour de Pise ?": "italie",
            "Quel est le plus long fleuve du monde ?": "amazone",
            "Quel pays a pour forme une botte ?": "italie",
            "Sur quel continent est le Kenya ?": "afrique",
            "Quelle est la monnaie du Royaume-Uni ?": "livre",
            "Quelle langue parle-t-on au Mexique ?": "espagnol",
            "Quel pays est connu pour ses kangourous ?": "australie",
            "Où se trouvent les pyramides de Gizeh ?": "egypte",
            "Quel est ce mot (Pa - Rat - Chut) ?": "parachute",
            "Je suis plein de trous mais je retiens l'eau. Qui suis-je ?": "eponge",
            "Qu'est-ce qui tombe sans faire de bruit ?": "nuit",
            "Plus il y en a, moins on voit. Qui suis-je ?": "obscurite",
            "J'ai des villes, mais pas de maisons. Des montagnes, mais pas d'arbres. Qui suis-je ?": "carte",
            "Qu'est-ce qui court sans jambes ?": "riviere",
            "Je commence la nuit et je finis le matin. Qui suis-je ?": "n",
            "Qu'est-ce qui a une tête mais pas de corps ?": "clou",
            "Je peux être d'eau, de sable ou d'heure. Qui suis-je ?": "grain",
            "Qu'est-ce qui s'allonge quand on le tire ?": "elastique",
            "Quel est le président de l'Inde (actuellement) ?": "droupadi murmu",
            "Qui fut le premier président de la France (Ve République) ?": "de gaulle",
            "Qui a découvert l'Amérique ?": "christophe colomb",
            "Quel empereur français a perdu à Waterloo ?": "napoleon",
            "Quelle reine d'Égypte a aimé César ?": "cleopatre",
            "Qui a peint la Joconde ?": "leonard de vinci",
            "En quelle année est tombé le mur de Berlin ?": "1989",
            "Qui a écrit 'Les Misérables' ?": "victor hugo",
            "Quel roi français a fini guillotiné ?": "louis xvi",
            "Qui a marché sur la lune en premier ?": "neil armstrong",
            "Combien de départements d’outre-mer compte la France ?": "5",
            "Quelle île française se trouve dans l'Océan Indien ?": "reunion",
            "Quel est le chef-lieu de la Martinique ?": "fort-de-france",
            "Quelle région d'outre-mer est en Amérique du Sud ?": "guyane",

            "Quel océan entoure Tahiti ?": "pacifique",
            "Quelle est la capitale de la Guadeloupe ?": "basse-terre",
            "De quel pays dépend Hawaï ?": "etats unis",
            "Quelle île est surnommée l'île de beauté ?": "corse",
            "Où se trouve Mayotte ?": "ocean indien",
            "Quelle est la fleur emblématique de Tahiti ?": "tiare",
            "Qu'est-ce qui est jaune et qui attend ?": "jonathan",
            "Quelle est la couleur du cheval blanc d'Henri IV ?": "blanc",
            "Qu'est-ce qui a des dents mais ne mord pas ?": "peigne",
            "Qu'est-ce qui monte et ne redescend jamais ?": "age",
            "Quel mois a 28 jours ?": "tous",
            "Qu'est-ce qui est vert, qui monte et qui descend ?": "petit pois",
            "Mme et Mr Terieur ont deux fils, comment s'appellent-ils ?": "alain et alex",
            "Quel est l'animal le plus heureux ?": "hibou",
            "Qu'est-ce qui court et qui se jette dans la mer ?": "fleuve",
            "Que fait une fraise sur un cheval ?": "tagada",
            "Quel est le symbole chimique de l'eau ?": "h2o",
            "Quelle planète est surnommée la planète rouge ?": "mars",
            "Qui a inventé l'ampoule électrique ?": "edison",
            "Quel est l'animal terrestre le plus rapide ?": "guepard",
            "Combien de continents y a-t-il sur Terre ?": "7",
            "Quel organe permet de pomper le sang ?": "coeur",
            "Quelle est la langue la plus parlée au monde ?": "mandarin",
            "Quel métal est liquide à température ambiante ?": "mercure",
            "Quel est le plus grand mammifère marin ?": "baleine bleue",
            "Combien de minutes y a-t-il dans une heure ?": "60"
        }

        clairiere.add_character(Character("Luci la fée", "une petite fée", clairiere, ["Bienvenue..."], questions_reponses))
        pont_arc.add_character(Character("Big Bob le Mage", "un mage", pont_arc, ["Prudence !"], questions_reponses))
        pierres_cristal.add_character(Character("Le Gardien de Cristal", "un être de pierre", pierres_cristal, ["Soyez patient."], questions_reponses))
        sentier_lanternes.add_character(Character("Le Veilleur des Lanternes", "un vieil esprit", sentier_lanternes, ["Esprit sauvage..."], questions_reponses))
        lac_miroir.add_character(Character("La Nymphe du lac", "une silhouette d'eau", lac_miroir, ["Le lac ne pardonne pas."], questions_reponses))
        jardins_fleurs.add_character(Character("La Dryade des Fleurs", "une créature végétale", jardins_fleurs, ["Réfléchissez..."], questions_reponses))
        grotte_lumineuse.add_character(Character("Chantal la Chèvre", "bruyante", grotte_lumineuse, ["Beheheheh !"], questions_reponses))

    def play(self):
        self.setup()
        self.print_welcome()
        self.player.quests.activate_quest("L'éveil de l'Arbre")
        self.player.quests.activate_quest("Collectionneur")
        
        while not self.finished:
            self.process_command(input("> "))
            self.player.quests.check_room_objectives(self.player.current_room.name)
            
            # On appelle loose(), mais on ne fait pas "break"
            # car loose() s'occupe déjà de téléporter le joueur.
            self.loose() 
                
            if self.win():
                break

    def process_command(self, command_string) -> None:
        if command_string.strip() == "":
            return
        list_of_words = [word for word in command_string.split(" ") if word]
        command_word = list_of_words[0]
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help'.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self):
        print(f"""
 Il était une fois {self.player.name}. {self.player.name} était une personne timide à l'école.
 Elle n'osait pas prendre la parole à haute voix devant ses camarades de classe ni devant ses profs.
 Elle voulait compter parmi les plus grands de ce monde mais elle se sentait prisonnière de ses propres chaînes.
 Un soir, elle pria tellement fort de changer de vie, d'être quelqu'un d'autre pour voir ce que cela faisait d'être courageuse. 
 Heureusement pour {self.player.name}, la Fée Emma entendit ses pleurs et décida de réaliser son vœu.
 
 {self.player.name} se réveilla dans une forêt enchantée où les lois physiques et intergalactiques se sont arrêtées.
 À ce moment-là, {self.player.name} savait qu'elle pouvait être qui elle voulait. 
 Et savez-vous qui est {self.player.name} ? Eh bien cette personne est vous ! On est tous {self.player.name} au fond de nous....

 Voici les règles claires du jeu de la Forêt Enchantée : 
 - Votre but est d'atteindre l'Arbre Ancien en ayant récupéré tous les objets présents dans chaque salle. 
 - Autrement dit, il vous faudra passer dans toutes les salles. Gare à vous si vous oubliez ne serait-ce qu'un objet ! 
 - Dans chaque salle dans laquelle vous accéderez, vous devez choisir dans quelle direction vous diriger. 
 - Attention ! On vous bloquera le passage car il faudra que vous répondiez à une question posée par un habitant du jeu !!! Vous aurez trois chances pour répondre correctement à l'habitant. C'est retour à la case départ sans aucun de vos objets!
 - Et surtout, la première chose que vous devez faire en accédant à une salle est de vérifier s'il y a un objet.

 Voici les différentes commandes pour cela dans le jeu :
    - help : afficher cette aide
    - quit : quitter le jeu
    - go <direction> : se déplacer (N, E, S, O)
    - history : afficher l'historique des pièces visitées
    - back : revenir à la pièce précédente
    - look : observer la pièce et voir les objets
    - take <item> : prendre un objet
    - drop <item> : déposer un objet
    - check : vérifier votre inventaire
    - quests : voir la progression des quêtes

 Bon jeu à toi !!
 """)
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

    def win(self):
        if self.player.current_room.name == "arbre ancien":
            quest_collectionneur = self.player.quests.get_quest_by_title("Collectionneur")
            if quest_collectionneur and quest_collectionneur.is_completed:
                print("\n🏆 Félicitations ! Vous avez atteint l'Arbre Ancien avec tous les objets !")
                print("La forêt s'illumine et vous devenez la nouvelle gardienne de ces lieux.")
                self.finished = True
                return True
        return False

    def loose(self):
        if self.player.current_room.name == "arbre ancien":
            quest_collectionneur = self.player.quests.get_quest_by_title("Collectionneur")
            
            if quest_collectionneur and not quest_collectionneur.is_completed:
                print("\n💀 L'Arbre Ancien vous rejette... Il vous manque des objets magiques !")
                print("La forêt vous renvoie au point de départ et vos objets retournent à leur place d'origine...")
                
                for item in self.player.inventory:
                    if hasattr(item, 'original_room') and item.original_room:
                        item.original_room.inventory.append(item)
                
                self.player.inventory.clear()
                self.player.current_room = self.rooms[0]
                print(self.player.current_room.get_long_description())
                return True
        return False
def main():
    Game().play()

if __name__ == "__main__":
    main()