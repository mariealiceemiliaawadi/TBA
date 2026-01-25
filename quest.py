""" Define the Quest class """

class Quest:
    """
    This class represents a quest in the game. A quest has a title, description,
    objectives, completion status, and optional rewards.
    """

    def __init__(self, title, description, objectives=None, reward=None):
        self.title = title
        self.description = description
        self.objectives = objectives if objectives is not None else []
        self.completed_objectives = []
        self.is_completed = False
        self.is_active = False
        self.reward = reward

    def activate(self):
        self.is_active = True
        print(f"\n🗡️  Nouvelle quête activée: {self.title}")
        print(f"📝 {self.description}\n")

    def complete_objective(self, objective, player=None):
        if objective in self.objectives and objective not in self.completed_objectives:
            self.completed_objectives.append(objective)
            print(f"✅ Objectif accompli: {objective}")

            # Check if all objectives are completed
            if len(self.completed_objectives) == len(self.objectives):
                self.complete_quest(player)

            return True
        return False

    def complete_quest(self, player=None):
        if not self.is_completed:
            self.is_completed = True
            print(f"\n🏆 Quête terminée: {self.title}")
            if self.reward:
                print(f"🎁 Récompense: {self.reward}")
                if player:
                    # Assurez-vous que la méthode add_reward existe dans votre classe Player
                    if hasattr(player, 'add_reward'):
                        player.add_reward(self.reward)
            print()

    def get_status(self):
        if not self.is_active:
            return f"❓ {self.title} (Non activée)"
        if self.is_completed:
            return f"✅ {self.title} (Terminée)"
        completed_count = len(self.completed_objectives)
        total_count = len(self.objectives)
        return f"⏳ {self.title} ({completed_count}/{total_count} objectifs)"

    def get_details(self, current_counts=None):
        details = f"\n📋 Quête: {self.title}\n"
        details += f"📖 {self.description}\n"

        if self.objectives:
            details += "\nObjectifs:\n"
            for objective in self.objectives:
                status = "✅" if objective in self.completed_objectives else "⬜"
                objective_text = self._format_objective_with_progress(objective, current_counts)
                details += f"  {status} {objective_text}\n"

        if self.reward:
            details += f"\n🎁 Récompense: {self.reward}\n"

        return details

    def _format_objective_with_progress(self, objective, current_counts):
        if not current_counts:
            return objective

        for counter_name, current_count in current_counts.items():
            if counter_name not in objective:
                continue

            required = self._extract_number_from_text(objective)
            if required is not None:
                return f"{objective} (Progression: {current_count}/{required})"

        return objective

    def _extract_number_from_text(self, text):
        for word in text.split():
            if word.isdigit():
                return int(word)
        return None

    def check_room_objective(self, room_name, player=None):
        room_objectives = [
            f"Visiter {room_name}",
            f"Explorer {room_name}",
            f"Aller à {room_name}",
            f"Entrer dans {room_name}"
        ]

        for objective in room_objectives:
            if self.complete_objective(objective, player):
                return True
        return False

    def check_action_objective(self, action, target=None, player=None):
        if target:
            objective_variations = [
                f"{action} {target}",
                f"{action} avec {target}",
                f"{action} le {target}",
                f"{action} la {target}"
            ]
        else:
            objective_variations = [action]

        for objective in objective_variations:
            if self.complete_objective(objective, player):
                return True
        return False

    def check_counter_objective(self, counter_name, current_count, player=None):
        for objective in self.objectives:
            if counter_name in objective and objective not in self.completed_objectives:
                required_count = self._extract_number_from_text(objective)
                if required_count is not None and current_count >= required_count:
                    self.complete_objective(objective, player)
                    return True
        return False

    def __str__(self):
        return self.get_status()


class QuestManager:
    def __init__(self, player=None):
        self.quests = []
        self.active_quests = []
        self.player = player

    def add_quest(self, quest):
        self.quests.append(quest)

    def activate_quest(self, quest_title):
        for quest in self.quests:
            if quest.title == quest_title and not quest.is_active:
                quest.activate()
                self.active_quests.append(quest)
                return True
        return False

    def complete_objective(self, objective_text):
        for quest in self.active_quests:
            if quest.complete_objective(objective_text):
                if quest.is_completed:
                    self.active_quests.remove(quest)
                return True
        return False

    def check_room_objectives(self, room_name):
        for quest in self.active_quests[:]:
            quest.check_room_objective(room_name, self.player)
            if quest.is_completed:
                self.active_quests.remove(quest)

    def check_action_objectives(self, action, target=None):
        for quest in self.active_quests[:]:
            quest.check_action_objective(action, target, self.player)
            if quest.is_completed:
                self.active_quests.remove(quest)

    def check_counter_objectives(self, counter_name, current_count):
        for quest in self.active_quests[:]:
            quest.check_counter_objective(counter_name, current_count, self.player)
            if quest.is_completed:
                self.active_quests.remove(quest)

    def get_active_quests(self):
        return self.active_quests

    def get_all_quests(self):
        return self.quests

    def get_quest_by_title(self, title):
        for quest in self.quests:
            if quest.title == title:
                return quest
        return None

    def show_quests(self):
        if not self.quests:
            print("\nAucune quête disponible.\n")
            return

        print("\n📋 Liste des quêtes:")
        for quest in self.quests:
            print(f"  {quest.get_status()}")
        print()

    def show_quest_details(self, quest_title, current_counts=None):
        quest = self.get_quest_by_title(quest_title)
        if quest:
            print(quest.get_details(current_counts))
        else:
            print(f"\nQuête '{quest_title}' non trouvée.\n")

    def check_quests(self):
        """
        Vérifie l'état de toutes les quêtes actives.
        Cette méthode est appelée par game.py après des événements importants.
        """
        for quest in self.active_quests[:]:
            if quest.is_completed:
                self.active_quests.remove(quest)