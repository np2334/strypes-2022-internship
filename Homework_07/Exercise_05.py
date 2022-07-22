import sys

if __name__ == "__main__":
    lines = []
    target_file = ""

    for i in range(1, len(sys.argv)):
        current_file_name = sys.argv[i]
        print(current_file_name)
        if not "dog_" in current_file_name:
            with open(current_file_name, "r") as reader:
                line = reader.readline()

                while line != '':
                    lines.append(line)
                    line = reader.readline()
        else:
            target_file = current_file_name

    with open(target_file, "a") as writer:
            for line in lines:
                writer.write("\n" + line)