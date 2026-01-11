import random

class Character:
    def __init__(self, name, description, current_room=None, msgs=None):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs if msgs else []

    def __str__(self):
        return f"{self.name} : {self.description}"

    # Méthode pour faire parler le PNJ cycliquement
    def get_msg(self):
        if not self.msgs:
            return f"{self.name} n'a rien à dire."
        
        # Prend le premier message et le remet à la fin pour cycle
        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg

    # Méthode pour déplacer le PNJ aléatoirement
    def move(self):
        if not self.current_room:
            return False
        if random.choice([True, False]):  # chance sur deux de se déplacer
            possible_rooms = [r for r in self.current_room.exits.values() if r]
            if possible_rooms:
                old_room = self.current_room
                new_room = random.choice(possible_rooms)
                old_room.characters.remove(self)
                new_room.characters.append(self)
                self.current_room = new_room
                return True
        return False