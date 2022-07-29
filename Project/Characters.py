class Entity:
    def __init__(self, health):
        self._health = health

    def __repr__(self):
        return "Health: {}".format(self._health)

    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage_points):
        if damage_points > 0:
            if self._health - damage_points < 0:
                self._health = 0
            self._health -= damage_points

class Character(Entity):
    def __init__(self, health, attack_power):
        super().__init__(health)
        self._max_health = health
        self._attack_power = attack_power
        self._effects = []

    def __repr__(self):
        return "Health: {}\tAttack_power: {}\nEffects: {}".format(self._health, self._attack_power, self._effects)

    def get_health(self):
        return self._health

    def get_attack_power(self):
        return self._attack_power

    def add_effect(self, effect):
        self._effects.append(effect)

    def __get__index_of_effect(self, effect):
        for i in range(0, len(self._effects)):
            if self._effects[i].get_name() == effect:
                return i
        return -1

    def remove_effect(self, effect):
        wanted_index = self.__get__index_of_effect(effect)
        return self._effects.pop(wanted_index)
        
    def get_effects(self):
        return self._effects

    def take_healing(self, healing_points):
        if self._health == 0 or healing_points < 0:
            return False

        if self._health + healing_points > self._max_health:
            self._health = self._max_health
        self._health += healing_points

        return True    

class Crusader(Character):
    def strike(self, target, strike):
        if self == target:
            return False

        target.take_damage(strike)
        return True

    def crusade_strike(self, target, crusade_strike):
        target.take_damage(int(crusade_strike[0]))

        # ако се използва crusader_strike върху собствения герой има обратен ефект - работи като buff
        is_buff = False
        if self == target:
            is_buff = True

        target.add_effect(Effect("Holy damage", int(crusade_strike[1]), int(crusade_strike[2]), is_buff))

    def holy_heal(self, target, holy_heal):
        if self != target:
            return False

        self.take_healing(holy_heal)
        return True



class DarkMagician(Character):
    def __init__(self, health, attack_power):
        super().__init__(health, attack_power)
        self.__is_imp_summoned = False
        self.__imp = None

    def shadow_bolt(self, target, shadow_bolt):
        if target == self:
            return False

        target.take_damage(shadow_bolt + shadow_bolt * self._attack_power)
        return True

    def drain_health(self, target, drain_health):
        if target == self:
            return False

        drained_health = drain_health * 3
        target.take_damage(drained_health)
        self.take_healing(drained_health)
        return True

    def summon_imp(self, target, summon_imp):
        if target != self:
            return False

        self.__is_imp_summoned = True
        self.__imp = Imp(summon_imp[0], summon_imp[1])
        return True



class Imp(Entity):
    def __init__(self, summon_imp):
        super().__init__(summon_imp[0])
        self.__damage = summon_imp[1]
    
    def do_damage(self, target, imp):
        target.take_damage(self.__damage)

    

class Effect:
    def __init__(self, name, round_duration, power, is_buff):
        self.__name = name
        self.__round_duration = round_duration
        self.__power = power
        self.__is_buff = is_buff

    def get_name(self):
        return self.__name

    # идеята ми е за всяко успешно използване на ефекта да връщам True и съответно щом върна False значи duration-a е изтекъл и мога да го махна от ефектите на target-a
    def activate_effect(self, target):
        if self.__round_duration == 0:
            print("\tEffect {} is over.".format(self.__name))
            target.remove_effect(self)
            return False

        effect_output = "Effect {} activated - ".format(self.__name)
        if self.__is_buff:
            target.take_healing(self.__power)
            effect_output += "healed for {}.".format(self.__power)
        else:
            target.take_damage(self.__power)
            effect_output += "{} damage taken.".format(self.__power)
        print(effect_output)

        self.__round_duration -= 1
        return True

