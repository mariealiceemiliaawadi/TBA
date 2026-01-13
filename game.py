# Description: Game class

DEBUG = False

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from quest import QuestManager


# --------------------------------------------------
# UTIL
# --------------------------------------------------
def normalize(text):
    if not text:
        return ""
    text = text.lower().strip()
    accents = {
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "à": "a", "â": "a", "ä": "a",
        "î": "i", "ï": "i",
        "ô": "o", "ö": "o",
        "ù": "u", "û": "u", "ü": "u",
        "ç": "c"
    }
    for a, b in accents.items():
        text = text.replace(a, b)
    return text


# --------------------------------------------------
# GAME
# --------------------------------------------------
class Game:

    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.quest_manager = QuestManager()

    # --------------------------------------------------
    # SETUP
    # --------------------------------------------------
    def setup(self):

        # Commands
        self.commands["help"] = Command("help", " : aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter", Actions.quit, 0)
        self.commands["go"] = Command("go", " <direction>", Actions.go, 1)
        self.commands["look"] = Command("look", " : observer", Actions.look, 0)
        self.commands["talk"] = Command("talk", " <pnj>", Actions.talk, -1)

        # Rooms
        clairiere = Room("clairiere", "dans une clairière illuminée par des lucioles.")
        pont_arc = Room("pont_arc", "sur un pont magique aux couleurs mouvantes.")
        lac_miroir = Room("lac_miroir", "près d’un lac reflétant l’âme.")
        sentier_lanternes = Room("sentier_lanternes", "sur un sentier hanté de lanternes.")
        pierres_cristal = Room("pierres_cristal", "devant des rochers lumineux.")
        jardins_fleurs = Room("jardins_fleurs", "dans un jardin enivrant.")
        grotte_lumineuse = Room("grotte_lumineuse", "dans une grotte scintillante.")
        arbre_ancien = Room("arbre_ancien", "au pied d’un arbre millénaire.")
        mare_brulee = Room("mare_brulee", "près d’une mare brûlante.")
        ruines_elfiques = Room("ruines_elfiques", "au milieu de ruines elfiques.")

        self.rooms = [
            clairiere, pont_arc, lac_miroir, sentier_lanternes,
            pierres_cristal, jardins_fleurs, grotte_lumineuse,
            arbre_ancien, mare_brulee, ruines_elfiques
        ]

        # Characters
        clairiere.add_character(Character(
            "Luci la fée", "une petite fée lumineuse", clairiere,
            msgs=["Bienvenue voyageur… la forêt t’observe."],
            question="Plus j’ai de gardiens, moins je suis en sécurité. Qui suis-je ?",
            answer="secret",
            hint="Quelque chose qu’on ne doit pas trop partager."
        ))

        pont_arc.add_character(Character(
            "Big Bob le Mage", "un mage à la cape changeante", pont_arc,
            msgs=["Attention à toi… Voici ta question !"],
            question="Combien font ((3*6)+4) / 11 ?",
            answer="2",
            hint="Commence par les parenthèses."
        ))

        pierres_cristal.add_character(Character(
            "Le Gardien de Cristal", "un être ancien de pierre", pierres_cristal,
            msgs=["Réfléchis bien avant de répondre."],
            question="Quelle est la capitale de l’Autriche ?",
            answer="vienne",
            hint="Ville de Mozart."
        ))

        sentier_lanternes.add_character(Character(
            "Le Veilleur des Lanternes", "un esprit silencieux", sentier_lanternes,
            msgs=["Réponds ou reste à jamais !"],
            question="Comment dit-on « le foie » en anglais ?",
            answer="liver",
            hint="Organe vital."
        ))

        lac_miroir.add_character(Character(
            "La Nymphe du lac", "silhouette translucide", lac_miroir,
            msgs=["Réponds avec lucidité…"],
            question="Quel est le pays le plus peuplé du monde ?",
            answer="inde",
            hint="Il a dépassé la Chine."
        ))

        jardins_fleurs.add_character(Character(
            "La Dryade des Fleurs", "créature végétale", jardins_fleurs,
            msgs=["Énigme en trois parties…"],
            question="Quel objet permet de voler après avoir sauté d’un avion ?",
            answer="parachute",
            hint="Sécurité aérienne."
        ))

        ruines_elfiques.add_character(Character(
            "La Méduse miraculeuse", "méduse spectaculaire", ruines_elfiques,
            msgs=["Attention à ma piqûre…"],
            question="Quel est le président de l’Inde ?",
            answer="droupadi murmu",
            hint="Première femme présidente."
        ))

        mare_brulee.add_character(Character(
            "La Fleur abandonnée", "fleur solitaire", mare_brulee,
            msgs=["Méfie-toi…"],
            question="Combien de territoires d’outre-mer compte la France ?",
            answer="5",
            hint="Tous hors d’Europe."
        ))

        grotte_lumineuse.add_character(Character(
            "Chantal la Chèvre", "chèvre bruyante", grotte_lumineuse,
            msgs=["Beheheh !"],
            question="Qu’est-ce qui est jaune et qui attend ?",
            answer="jonathan",
            hint="Blague très connue."
        ))

        # Exits
        clairiere.exits = {"N": pont_arc}
        pont_arc.exits = {"E": pierres_cristal, "O": lac_miroir, "S": jardins_fleurs}
        pierres_cristal.exits = {"N": jardins_fleurs}
        jardins_fleurs.exits = {"E": ruines_elfiques}
        ruines_elfiques.exits = {"N": arbre_ancien, "E": grotte_lumineuse, "S": mare_brulee}
        mare_brulee.exits = {"N": ruines_elfiques}

        # Player
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = pont_arc

    # --------------------------------------------------
    # WELCOME
    # --------------------------------------------------
    def print_welcome(self):
        print(f"\n🌲 Bienvenue {self.player.name} dans la Forêt Enchantée 🌲\n")
        print("📜 RÈGLES DU JEU :")
        print("- Chaque salle contient une énigme.")
        print("- Tu as 3 tentatives maximum.")
        print("- En cas d’échec, tu recules.")
        print("- Tant que l’énigme n’est pas résolue, tu ne peux pas avancer.")
        print("- Le mot magique pour un indice est : abracadabra 🪄\n")
        print(self.player.current_room.get_long_description())

    # --------------------------------------------------
    # PLAY
    # --------------------------------------------------
    def play(self):
        self.setup()
        self.print_welcome()

        while not self.finished:
            room = self.player.current_room

            if room.characters:
                c = room.characters[0]
                if c.question and not c.solved:
                    print(f"\n👤 {c.name} — {c.description}")
                    print(c.get_msg())
                    print(f"❓ {c.question}")

                    while c.attempts < 3:
                        answer = input("> ").strip()

                        # 🔴 Quit immédiat même pendant une énigme
                        if answer.lower() == "quit":
                            print("\n👋 Tu abandonnes l’épreuve. À bientôt.\n")
                            self.finished = True
                            return

                        # 🪄 Indice
                        if normalize(answer) == "abracadabra":
                            print(f"💡 Indice : {c.hint}")
                            continue



                        c.attempts += 1
                        if normalize(answer) == normalize(c.answer):
                            print("✅ Bonne réponse !\n")
                            c.solved = True
                            break
                        else:
                            print(f"❌ Faux ({3 - c.attempts} essais restants)")

                    if not c.solved:
                        print("☠️ Trop d’erreurs, tu recules.\n")
                        return

            cmd = input("> ")
            self.process_command(cmd)

            if self.win():
                print("\n🏆 FÉLICITATIONS, TU AS GAGNÉ ! 🏆\n")
                self.finished = True

    # --------------------------------------------------
    def process_command(self, command_string):
        words = command_string.split()
        if not words:
            return
        cmd = words[0]
        if cmd in self.commands:
            self.commands[cmd].action(self, words, self.commands[cmd].number_of_parameters)
        else:
            print("Commande inconnue.")

    # --------------------------------------------------
    def win(self):
        return self.player.current_room.name == "arbre_ancien"


# --------------------------------------------------
def main():
    Game().play()


if __name__ == "__main__":
    main()
