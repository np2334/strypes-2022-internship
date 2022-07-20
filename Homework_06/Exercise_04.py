import Exercise_04_classes
import inspect

#TODO with eval and refletion
# dir -> functions
# inspect.signature(Test.__init__))
# a.parameters 
# for k in a.parameters:


game_classes = ["Hero", "Orc"]
#game_classes_dictionary = {
#    "Hero": 
#}

print("Simple python class game\n\nAvailable classes: ")
for character_class in game_classes:
    print("\t" + character_class)

print("\nPlayer1:\n\tSelect class:")
hero_one = input()

inspect.signature(obj)

#print(isinstance(hero_one, Exercise_04_classes.Orc))
#print(isinstance(hero_one, Exercise_04_classes.Hero))

