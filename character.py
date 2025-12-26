class Character:
    def __init__(self, name, description, messages):
        self.name = name
        self.description = description
        self.messages = messages

    def __str__(self):
        return f"{self.name} : {self.description}"

    def talk(self):
        if len(self.messages) > 0:
            return self.messages[0]
        return ""