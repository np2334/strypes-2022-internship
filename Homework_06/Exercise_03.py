import Exercise_03_entity

hero = Exercise_03_entity.Hero("Bron", 100, "DragonSlayer")
print(hero)
hero.take_damage(20)

orc = Exercise_03_entity.Orc("Orc", 120, 1.1)
print(orc.inflict_damage(10))

