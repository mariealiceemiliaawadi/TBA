# TBA - Jeu d'Aventure Textuel avec Système de Quêtes

Ce projet est un jeu d'aventure textuel (TBA) se déroulant dans un univers magique. Vous incarnez Alice, une jeune fille timide transformée en héroïne par la fée Emma, et devez explorer une forêt mystérieuse pour accomplir votre destinée.


## Histoire

Alice était une personne timide qui n'osait pas prendre la parole. Un soir, elle pria pour devenir courageuse. La fée Emma exauça son vœu et Alice se réveilla dans une forêt enchantée où les lois physiques sont suspendues. Cette personne, c'est vous.


## Description

Ce document décrit une version immersive du jeu d’aventure textuel TBA (Text-Based Adventure), plongeant le joueur dans le récit d'Alice, une jeune fille timide propulsée dans une Forêt Enchantée par la fée Emma. Dans cet univers où les lois physiques et intergalactiques s'arrêtent, le joueur doit faire preuve de courage et de rigueur pour progresser.

Le joueur explore une carte composée de zones mystérieuses interconnectées, interagit avec des objets magiques et rencontre des habitants (PNJ) comme la fée Luci. Cette version intègre des mécaniques de jeu avancées :

  - Système de collecte obligatoire : Obligation de vider chaque salle de ses objets avant de pouvoir avancer.

  - Énigmes narratives : Interactions avec les habitants nécessitant des réponses précises sous peine de sanctions.

  - Gestion de l'historique : Possibilité de consulter son parcours et de revenir sur ses pas.

  - Suivi de quêtes dynamique : Un système complet permettant de suivre simultanément des objectifs de collection (les 7 objets magiques) et de destination (l'Arbre Ancien).

Cette version constitue une base solide et fonctionnelle, pensée pour offrir une expérience narrative forte tout en restant une structure technique évolutive.


**État actuel du projet (branche `tba-quests`) :**
- 8 lieux explorables et interconnectés
- Navigation par directions cardinales (N, E, S, O)
- **Système de quêtes complet** avec objectifs et récompenses
- Gestion des quêtes actives et complétées
- Suivi automatique de la progression des objectifs
- Statistiques de déplacement du joueur

Cette version introduit un système de quêtes qui enrichit considérablement l'expérience de jeu et sert de base pour des mécaniques plus complexes.

## Règles du jeu

Le jeu impose des conditions strictes pour progresser dans la Forêt Enchantée :

  - Exploration exhaustive : Vous devez récupérer tous les objets présents dans chaque salle avant de pouvoir la quitter. Si vous oubliez ne serait-ce qu'un objet, le passage vous sera refusé.

  - Énigmes et Habitants : Le passage vers certaines zones est bloqué par des habitants. Vous devrez répondre correctement à leurs questions.

  - Droit à l'erreur : Vous disposez de 3 chances pour répondre correctement à un habitant.

  - Conséquence de l'échec : En cas d'échec critique (0 chance restante), vous êtes automatiquement renvoyé à la case de départ et vous perdez tous vos objets !

Premier réflexe : La première chose à faire en arrivant dans une salle est de vérifier s'il s'y trouve un objet (look).


## Lancement du jeu

Pour démarrer le jeu, exécuter simplement :
```bash
python game.py
```

## Commandes disponibles

### Commandes de base
- `help` : Afficher l'aide et la liste des commandes
- `quit` : Quitter le jeu
- `go <direction>` : Se déplacer dans une direction (N, E, S, O)
- `back` : Revenir en arrière
- `look` : Observer la pièce
- `take <objet>` : Ramasser un objet
- `drop <objet>` : Déposer un obje
- `check` : Consulter l’inventaire
- `talk <personnage>` : Parler à un PNJ
- `history` : Consulter l’historique

### Commandes de quêtes
- `quests` : Afficher la liste de toutes les quêtes disponibles
- `quest <titre>` : Afficher les détails d'une quête spécifique
- `activate <titre>` : Activer une quête pour commencer à la suivre

### Commandes spéciales pour les énigmes
- `abracadabra` : Obtenir un indice pour résoudre l’énigme de la salle actuelle


## Système de Quêtes

Le système de quêtes permet de :
- Définir des objectifs à accomplir
- Suivre automatiquement la progression
- Gérer plusieurs quêtes simultanément
- Obtenir des récompenses à la completion

Dans le conexte de notre jeu, nous avons deux quêtes principales : 
  - L'éveil de l'Arbre : Atteindre l'Arbre Ancien pour terminer l'aventure.

  - Collectionneur : Récupérer les 7 objets magiques dissimulés dans les différentes salles de la forêt.

**Types d'objectifs disponibles :**
- Objectifs de visite : visiter un lieu spécifique
- Objectifs de compteur : effectuer une action un certain nombre de fois (ex: se déplacer 10 fois)

## Structuration

Le projet est organisé en 6 modules contenant chacun une ou plusieurs classes :

### Modules principaux

- **`game.py` / `Game`** : Gestion de l'état du jeu, de l'environnement et de l'interface avec le joueur
- **`room.py` / `Room`** : Propriétés génériques d'un lieu (nom, description, sorties)
- **`player.py` / `Player`** : Représentation du joueur avec gestion des déplacements et intégration du QuestManager
- **`command.py` / `Command`** : Structure des commandes avec leurs paramètres et actions associées
- **`actions.py` / `Actions`** : Méthodes statiques définissant toutes les actions exécutables (déplacements, gestion des quêtes, etc.)
- **`quest.py`** : 
  - `Quest` : Représentation d'une quête avec ses objectifs
  - `Objective` : Classe de base pour les objectifs
  - `RoomObjective` : Objectif de visite d'un lieu
  - `CounterObjective` : Objectif basé sur un compteur
  - `QuestManager` : Gestionnaire des quêtes du joueur

## Architecture

Le jeu utilise une architecture orientée objet avec gestion d'événements :

1. **Game** initialise le jeu et les quêtes disponibles
2. **Player** contient un `QuestManager` qui suit les quêtes actives
3. **QuestManager** vérifie automatiquement la progression lors des actions du joueur
4. **Objectives** définissent différents types de conditions à remplir
