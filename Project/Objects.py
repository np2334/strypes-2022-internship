import inspect
import json
from time import sleep
from os import system, name
from Characters import DarkMagician, Crusader

class Game:
    def __init__(self):
        self.__number_of_players = int(self.__get_number_of_players())

        self.__available_classes = self.__get_available_classes()

        self.__player_saves = {}
        self.__get_player_saves()

        self.__players = []
        for i in range(0, self.__number_of_players):
            self.__configure_player(i + 1)

        for player in self.__players :
            print(player)
        
        print("\nGame starting in...", end = "")
        for i in range(3, 0, -1):
            print(" {} ".format(i), end = "")
            sleep(2)

        self.__start_game()

    def __is_one_player_remaining(self):
        alive_players_count = 0
        for player in self.__players:
            if player.get_selected_class().is_alive():
                alive_players_count += 1

                # значи имаме два или повече живи играча
                if alive_players_count > 1:
                    return False
        return True
    
    def __get_target_class_instance(self, target_player):
        for player in self.__players:
            if player.get_name() == target_player:
                return player.get_selected_class()

    def __get_winner(self):
        for player in self.__players:
            if player.get_selected_class().is_alive():
                return player

    def __start_game(self):
        is_one_player_remaining = False
        while not is_one_player_remaining:
            for player in self.__players:
                self.__clear()

                # TODO effect за пропускане
                # ако героя на текущия играч е загинал пропуска хода
                if not player.get_selected_class().is_alive():
                    continue
                
                local_players = []
                for local_player in self.__players:
                    if local_player.get_name() == player.get_name() or not local_player.get_selected_class().is_alive():
                        continue
                    local_players.append(local_player.get_name())

                # за всеки ефект върху героя
                for effect in player.get_selected_class().get_effects():
                    effect.activate_effect(player.get_selected_class())

                print("Current turn:\n{}".format(player, local_players))

                print("\n\nLocal players: {}\nUse ability on player: ".format(local_players), end = "")
                target_player = input()

                while not target_player in local_players:
                    print("{} is not valid entity.\nUse ability on player: ".format(target_player, local_players), end = "")
                    target_player = input()

                print("\nSelect one of the following abilities:")
                available_abilites = self.__available_classes[type(player.get_selected_class()).__name__]["abilities"]
                for ability in available_abilites:
                    print("\t{}".format(ability))
                print("\nAbility: ", end = "")

                selected_ability = input()
                while not selected_ability in available_abilites:
                    print("Choose ability from the list above...")
                    print("\nAbility: ", end = "")
                    selected_ability = input()


                target_class_instance = self.__get_target_class_instance(target_player)
                target_class_instance_health = target_class_instance.get_health()

                # примерно при Crusade Strike имаме лист с 3 стойности - "crusade_strike": ["8", "2", "3"]
                # стойност, която се взима на момента, стойност на ефект за всеки рунд и брой на рундовете, за които важи ефекта
                selected_ability_arguments = available_abilites[selected_ability]

                #current_instance.some_ability(target_instance, [12, 3, 3])
                eval("player.get_selected_class().{}(target_class_instance, {})".format(selected_ability, selected_ability_arguments))

                print("\nPlayer {} used {} on {} and did {} damage.\n".format(player.get_name(), selected_ability, target_player, target_class_instance_health - target_class_instance.get_health()))
                sleep(2)
            is_one_player_remaining = self.__is_one_player_remaining()

            winner = self.__get_winner()
            for player in self.__players:
                if player.get_name() != winner.get_name():
                    player.add_loss()
                else:
                    player.add_win()

            self.__clear()

            print("{} has won the game! Congratulations!\n{}\nWould you like to save the result? (Y/N): ".format(winner.get_name(), winner), end = "")
            should_save = input()

            while not should_save in ['Y', 'N']:
                self.__clear()
                print("{} has won the game! Congratulations!\n{}\nWould you like to save the result? (Y/N): ".format(winner.get_name(), winner), end = "")
                should_save = input()

            if should_save == 'Y':
                # TODO
                pass


    def __clear(self):
    # ако е windows
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def __get_number_of_players(self):
        print("Enter number of players: ", end = "")
        number_of_players = input()
        while not number_of_players.isnumeric() or number_of_players == "0" or number_of_players == "1":
            self.__clear()
            print("Please enter valid player count!\nEnter number of players: ", end = "")
            number_of_players = input()
        self.__clear()
        return number_of_players

    def __get_available_classes(self):
        with open("game_classes_config.json", "r") as reader:
            return json.load(reader)

    # зареждам в началото всички налични save-ове
    def __get_player_saves(self):
        with open("save.txt", "r") as reader:
            line = reader.readline()
            
            while line != "":
                # форматът е име=[брой победи, брой загуби]
                line_arguments = line.split("=")
                player_name = line_arguments[0]
                player_stats = eval(line_arguments[1])

                self.__player_saves[player_name] = player_stats

                line = reader.readline()

    def __initialize_class(self):
        selected_class = ""
        while not selected_class in self.__available_classes:
            self.__clear()
            print("List of available classes: ")
            for available_class in self.__available_classes:
                print("\t{}".format(available_class))
            print("\nWrite TODO !info class_name TODO to get detailed information about the class or class_name to select the wanted class.\nSelect class: ", end = "")

            line = input()
            selected_class = line
            #line_arguments = line.split(" ")


        # започвам да създавам initalization expression за дадения клас
        # примерно Crusader(
        class_initalization_expression = "{}(".format(selected_class)
        # inspect-вам конструктора на дадения клас
        class_ctor = inspect.signature(eval("{}.__init__".format(selected_class)))

        class_ctor_parameters = []
        for current_parameter in class_ctor.parameters:
            if current_parameter == "self":
                continue

            # за всеки параметър на дадения клас добавям динамично стойността на параметъра от json-a, примерно available_classes[Crusader][health], available_classes[Crusader][attack_power]
            class_ctor_parameters.append(self.__available_classes[selected_class][current_parameter])
        # добавям параметрите 
        # примерно Crusader(135, 0.0
        class_initalization_expression += ", ".join(class_ctor_parameters)
        # добавям липсващата скоба отдясно
        # примерно Crusader(135, 0.0)
        class_initalization_expression += ")"

        return eval(class_initalization_expression)

    def __is_player_name_unique(self, name):
        for player in self.__players:
            if player.get_name() == name:
                return False
        return True

    # взимам под формата на input нужната информация за създаване на player
    def __configure_player(self, player_number):
        print("Enter name for Player {}: ".format(player_number), end = "")
        player_name = input()

        while not self.__is_player_name_unique(player_name):
            self.__clear()
            print("Please enter unique name!\nEnter name for Player {}: ".format(player_number), end = "")
            player_name = input()

        self.__clear()

        player_wins = 0
        player_losses = 0

        # ако има запазен save с името на player-a
        if not (self.__player_saves.get(player_name) == None):
            player_wins = self.__player_saves.get(player_name)[0]
            player_losses = self.__player_saves.get(player_name)[1]

            print("Player save found for {}: {} wins\t{} losses".format(player_name, player_wins, player_losses))
            sleep(3)
            self.__clear()

        # докато не се въведе валиден клас
        selected_class = self.__initialize_class()

        self.__players.append(Player(player_name, selected_class, player_wins, player_losses))
        self.__clear()

    def get_players(self):
        return self.__players



class Player:
    def __init__(self, name, selected_class, wins, losses):
        self.__name = name
        self.__selected_class = selected_class
        self.__wins = wins
        self.__losses = losses

    def __repr__(self):
        return "Player {}, selected class: {}\nHealth: {}\tAttack Power: {}\nWins: {}\tLosses: {}\n".format(self.__name, 
                                                                                                            type(self.__selected_class).__name__, 
                                                                                                            self.__selected_class.get_health(),
                                                                                                            self.__selected_class.get_attack_power(),
                                                                                                            self.__wins, 
                                                                                                            self.__losses)

    def get_selected_class(self):
        return self.__selected_class

    def add_win(self):
        self.__wins += 1

    def add_loss(self):
        self.__losses += 1

    def get_name(self):
        return self.__name

