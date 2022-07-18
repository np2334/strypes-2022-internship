def manage_marbles(list_of_marbles):
    dictionary_of_marbles = {}
    for marble_pair in list_of_marbles:
        color = marble_pair[0]
        count = marble_pair[1]

        if dictionary_of_marbles.get(color) == None:
            dictionary_of_marbles[color] = 0
        dictionary_of_marbles[color] += count
    return dictionary_of_marbles

marbles = [("red", 3), ("blue", 2), ("yellow", 10), ("red", 7), ("green", 8), ("blue", 5)]
print(manage_marbles(marbles))