# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

import unicodedata



class Actions:

    @staticmethod
    def strip_accents(s):
        return "".join(c for c in unicodedata.normalize('NFD', s)
                      if unicodedata.category(c) != 'Mn')

    @staticmethod
    @staticmethod
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        player = game.player
        direction = list_of_words[1].upper()
        next_room = player.current_room.exits.get(direction)

        if next_room:
            if player.current_room.characters:
                character = list(player.current_room.characters.values())[0]
                attempts = 0
                success = False
                
                while attempts < 3:
                    result = character.get_question(game)
                    if result == "QUIT":
                        return
                    if result is True:
                        success = True
                        break
                    else:
                        attempts += 1
                        if attempts < 3:
                            print(f"Mauvaise réponse ! Il vous reste {3 - attempts} essai(s).")
                
                if success:
                    player.current_room = next_room
                    player.history.append(player.current_room)
                    print(f"Bonne réponse ! Vous entrez dans : {next_room.name}")
                    print(player.current_room.get_long_description())
                else:
                    print("\nÉCHEC ! Vous repartez de zéro et les objets retournent dans la forêt.")
                    
                    for item in player.inventory:
                        if hasattr(item, 'original_room') and item.original_room:
                            item.original_room.inventory.append(item)
    
                    player.inventory.clear()
                    player.current_room = game.rooms[0]
                    print(player.current_room.get_long_description())
            else:
                player.current_room = next_room
                print(player.current_room.get_long_description())
        else:
            print("Il n'y a pas de sortie par là.")

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def look(game, list_of_words, number_of_parameters):
        game.player.current_room.look()
        return True
    
    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        player = game.player
        if len(list_of_words) < 2:
            print(MSG1.format(command_word=list_of_words[0]))
            return False
        
        item_name = " ".join(list_of_words[1:])
        
        success = player.take(item_name)
        if success:
            game.player.quests.check_action_objectives("Prendre", item_name)
        return success

    def drop(game, list_of_words, number_of_parameters):
        player = game.player
        if len(list_of_words) < 2:
            print(MSG1.format(command_word=list_of_words[0]))
            return False
            
        item_name = " ".join(list_of_words[1:])
        
        success = player.drop(item_name)
        return success

    def check(game, list_of_words, number_of_parameters):
        print(game.player.get_inventory())
        return True

    def quests(game, list_of_words, number_of_parameters):
        # On affiche simplement la liste des quêtes du joueur
        game.player.quests.show_quests()
        return True

    def quit(game, list_of_words, number_of_parameters):
        game.finished = True
        print(f"Merci d'avoir joué, {game.player.name} !")
        return True