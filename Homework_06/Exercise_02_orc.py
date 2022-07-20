class Orc:
    def __init__(self, name, health, berserk_factor):
        self.__name = name
        self.__health = health
        self.__max_health = health

        self.__berserker_factor = 0
        if berserk_factor > 2:
            self.__berserk_factor = 2
        elif berserk_factor < 1:
            self.__berserk_factor = 1
        else:
            self.__berserk_factor = berserk_factor  

    def get_health(self):
        return self.__health
    
    def is_alive(self):
        return self.__health > 0

    def inflict_damage(self, damage):
        return self.__berserk_factor * damage

    def take_damage(self, damage_points):
        if damage_points > 0:
            if self.__health - damage_points < 0:
                self.__health = 0
            self.__health -= damage_points

    def take_healing(self, healing_points):
        if self.__health == 0 or healing_points < 0:
            return False

        if self.__health + healing_points > self.__max_health:
            self.__health = self.__max_health
        self.__health += healing_points

        return True