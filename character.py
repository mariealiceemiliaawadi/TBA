import random

class Character:
    def __init__(self, name, description, current_room, msgs, questions_dict):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.msg_index = 0
        self.questions_dict = questions_dict

    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        if not self.msgs:
            return "Il ne semble pas vouloir parler."
        message = self.msgs[self.msg_index]
        self.msg_index = (self.msg_index + 1) % len(self.msgs)
        return message

    def get_question(self, game):
        question = random.choice(list(self.questions_dict.keys()))
        reponse_correcte = self.questions_dict[question]
        
        print(f"\n{self.name} vous pose une question :")
        print(f"'{question}'")
        
        reponse_joueur = input("Votre réponse : ").strip().lower()
        
        if reponse_joueur == "quit":
            game.finished = True
            return "QUIT"
        
        import unicodedata
        def normalize(text):
            return "".join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

        if normalize(reponse_joueur) == normalize(reponse_correcte.lower()):
            return True
        else:
            return False