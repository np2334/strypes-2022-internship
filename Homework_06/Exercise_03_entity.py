class Entity:
    def __init__(self, name, health):
        self._name = name
        self._health = health
        self._max_health = health
        
    # _ protected __ private
    #def get_name(self):
    #    return self.__name

    def get_health(self):
        return self._health
    
    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage_points):
        if damage_points > 0:
            if self._health - damage_points < 0:
                self._health = 0
            self._health -= damage_points

    def take_healing(self, healing_points):
        if self._health == 0 or healing_points < 0:
            return False

        if self._health + healing_points > self._max_health:
            self._health = self._max_health
        self._health += healing_points

        return True

class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.__nickname = nickname

    def __repr__(self):
        return "{} the {}".format(self._name, self.__nickname)


class Orc(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.__berserk_factor = berserk_factor

    def inflict_damage(self, damage):
        return self.__berserk_factor * damage    