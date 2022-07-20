import Exercise_02_orc

orc = Exercise_02_orc.Orc("Random orc name", 100, 1.23)

print(orc)
print(orc.get_health())
orc.take_damage(12)
print(orc.get_health())

print(orc.inflict_damage(50))