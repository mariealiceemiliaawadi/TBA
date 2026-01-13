import random

class Character:
    def __init__(
        self,
        name,
        description,
        current_room=None,
        msgs=None,
        question=None,
        answer=None,
        hint=None
    ):
        self.name = name
        self.description = description
        self.current_room = current_room

        # Messages d’introduction (affichés avant la question)
        self.msgs = msgs if msgs else []

        # 🔹 SYSTÈME DE QUESTION
        self.question = question
        self.answer = answer
        self.hint = hint

        self.solved = False       # La question a-t-elle été résolue ?
        self.attempts = 0         # Nombre de tentatives utilisées (max 3)

    def __str__(self):
        return f"{self.name} : {self.description}"

    # 🔹 Message cyclique (comme avant)
    def get_msg(self):
        if not self.msgs:
            return f"{self.name} n'a rien à dire."

        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg

    # 🔹 Indique si ce PNJ bloque la salle avec une question
    def has_question(self):
        return self.question is not None and not self.solved

    # 🔹 Réinitialisation (si tu veux un reset plus tard)
    def reset_question(self):
        self.solved = False
        self.attempts = 0

    # 🔹 Déplacement aléatoire des PNJ (inchangé)
    def move(self):
        if not self.current_room:
            return False

        if random.choice([True, False]):  # 1 chance sur 2 de bouger
            possible_rooms = [r for r in self.current_room.exits.values() if r]
            if possible_rooms:
                old_room = self.current_room
                new_room = random.choice(possible_rooms)

                old_room.characters.remove(self)
                new_room.characters.append(self)
                self.current_room = new_room
                return True

        return False
