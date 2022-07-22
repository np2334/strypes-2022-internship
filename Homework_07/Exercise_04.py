import sys

if __name__ == "__main__":
    arguments = []
    for i in range(1, len(sys.argv)):
        arguments.append(sys.argv[i])

    with open("arguments.txt", "a") as writer:
        for argument in arguments:
            writer.write(argument + "\n")