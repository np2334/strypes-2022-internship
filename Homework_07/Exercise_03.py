with open("dog_breeds.txt", "a") as writer:
    writer.write("\nNew breed")

with open("dog_breeds.txt", "r") as reader:
    line = reader.readline()

    while line != '':
        print(line)
        line = reader.readline()

